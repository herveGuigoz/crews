# CrewAI Utilities

A collection of AI-powered multi-agent systems built with [crewAI](https://crewai.com). This project demonstrates how multiple AI agents can collaborate to automate various tasks using specialized crews.

## Available Crews

### Recipe From YouTube

An AI-powered crew that extracts YouTube video transcripts and converts them into well-formatted recipes in French.

**Features:**
- Transcript extraction from YouTube videos
- Recipe generation with structured ingredients and instructions in French
- Multi-agent collaboration between transcript extractor and recipe writer

**Usage:**
```bash
uv run youtube_transcript
```

## Prerequisites

- Python >=3.10 <3.14
- [uv](https://docs.astral.sh/uv/) for dependency management
- OpenAI API key

## Installation

### 1. Install Dependencies

```bash
uv sync
```

This will create a virtual environment and install all required dependencies automatically.

### 2. Configure Environment Variables

Create a `.env` file in the project root with your OpenAI API configuration:

```bash
# Create .env file
cat > .env << EOF
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini
EOF
```

Or manually create the `.env` file with these variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE_URL=https://api.openai.com/v1  # Optional, defaults to OpenAI
MODEL_NAME=gpt-4o-mini  # Optional, defaults to gpt-4o-mini
```

**Important:** Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Project Structure

```
crew-ai/
├── src/
│   └── crews/
│       ├── config/
│       │   ├── agents.yaml      # Agent configurations
│       │   └── tasks.yaml       # Task definitions
│       ├── tools/
│       │   ├── __init__.py
│       │   └── custom_tool.py   # Custom tools for crews
│       ├── __init__.py
│       ├── crew.py              # Crew definitions
│       └── main.py              # Entry points for crews
├── pyproject.toml               # Poetry dependencies and project metadata
├── .env                         # Environment variables (create this)
└── README.md
```

## Adding New Crews

To add a new crew to this collection:

1. **Define Agents**: Add agent configurations to `src/crews/config/agents.yaml`
2. **Define Tasks**: Add task configurations to `src/crews/config/tasks.yaml`
3. **Create Crew Class**: Add a new crew class in `src/crews/crew.py` using the `@CrewBase` decorator
4. **Add Entry Point**: Create a run function in `src/crews/main.py`
5. **Register Script**: Add a new script entry in `pyproject.toml` under `[project.scripts]`
6. **Create Custom Tools** (if needed): Add tools to `src/crews/tools/`

### Example Crew Structure

```python
@CrewBase
class MyNewCrew():
    """MyNewCrew description"""

    @agent
    def my_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['my_agent'],
            verbose=True
        )

    @task
    def my_task(self) -> Task:
        return Task(
            config=self.tasks_config['my_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
```

## Development

### Activating the Virtual Environment

```bash
# uv automatically uses the virtual environment
# No need to activate manually when using uv run
uv run python
```

Or activate it manually:

```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

### Adding Dependencies

```bash
uv add package-name
```

### Removing Dependencies

```bash
uv remove package-name
```

### Updating Dependencies

```bash
uv sync --upgrade
```

### Running a Specific Crew

Each crew has its own command registered in `pyproject.toml`. Check the `[project.scripts]` section for available commands.

```bash
# Run with uv
uv run youtube_transcript

# Or if you activated the virtual environment
youtube_transcript
```

## Customization

### Modifying Agents

Edit `src/crews/config/agents.yaml` to customize agent roles, goals, and backstories.

### Modifying Tasks

Edit `src/crews/config/tasks.yaml` to change task descriptions and expected outputs.

### Adding Custom Tools

Create new tools in `src/crews/tools/` by extending `BaseTool` from crewAI:

```python
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MyCustomToolInput(BaseModel):
    argument: str = Field(..., description="Description of the argument")

class MyCustomTool(BaseTool):
    name: str = "My Custom Tool"
    description: str = "Description of what the tool does"
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation
        return result
```

## How CrewAI Works

CrewAI enables you to create autonomous AI agents that work together as a crew to accomplish complex tasks. Each crew consists of:

- **Agents**: AI entities with specific roles, goals, and backstories
- **Tasks**: Specific jobs assigned to agents with clear descriptions and expected outputs
- **Tools**: Capabilities that agents can use to perform their tasks
- **Process**: How agents collaborate (sequential, hierarchical, etc.)

## Support

For support, questions, or feedback:
- Visit the [crewAI documentation](https://docs.crewai.com)
- Check out the [crewAI GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join the crewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## License

This project is open source and available under the MIT License.
