# AI Research Workflow

A framework for AI-aided research using **context engineering** to guide AI agents for coding, data analysis, image analysis, and scientific computing. This repository demonstrates how to move beyond simple prompting to sophisticated agent-based workflows using rules, skills, MCPs, and subagents. The key philosophy is to provide the right structure, rules, and tools so AI agents work autonomously and reliably on complex research tasks.

In this repository you will find information about:

- **Rules**: Instructions that guide AI behavior in generating code, editing files, and creating files. Located in `.cursor/rules/`. Rules are written in markdown in multiple files, each focusing on specific tasks. For example, `project-repo.mdc` guides the AI on how to organize the project repository. `python-coding-standards.mdc` specifies coding standards and best practices. The main rule, `rules.mdc`, specifies the project goals and lists all available rules, skills, subagents, MCPs, and commands.
- **Tool Integration**: Connecting AI to MCPs (Model Context Protocol) to leverage specialized tools for complex tasks, such as `napari-mcp` (image visualization), `cellpose` (cell segmentation), `sympy-mcp` (symbolic math), and `fmcp` (scientific plotting). See [mcpservers.org](https://mcpservers.org).
- **Plan**: Plans allow you to get a more structured and detailed, step-by-step to-do list for the AI to follow. This helps move from vague prompts to structured execution, significantly improving code quality.
- **Subagents**: Specialized agents that run in the background and interact with the main agent. They do not share the main agent's context window, preserving memory. For example, the `literature-review` subagent searches literature and provides citations.
- **Skills**: Reusable capabilities providing domain-specific tools and knowledge. For example, scientific writing skills for LaTeX or cluster execution.
- **Commands**: Shortcuts for repetitive tasks that don't require deep reasoning. For example, the `/git` command helps with version control.

## Repository Structure

```
AI Research Workflow/
├── .cursor/
│   ├── rules/                  # Persistent AI guidance
│   │   ├── rules.mdc           # Main project rules & expert domains
│   │   ├── python-coding-standards.mdc
│   │   ├── Image-analysis.mdc  # Image analysis patterns
│   │   └── project-repo.mdc    # Project structure guide
│   ├── agents/                 # Specialized agents
│   │   └── literature-review.md
│   ├── commands/               # Command shortcuts
│   │   └── git.md
│   └── skills/                 # Reusable capabilities
│       └── scientific-writing/
├── Data_analysis/
│   ├── road_accident_dataset.csv
│   └── prompt.md
├── Image_analysis/
│   └── demo_images/            # 23 sample images
├── deep_stuff/
│   └── rules_of_life.md
└── workflow.ipynb              # Workflow notebook
```

## Example Workflows

### Data Analysis
- Rules define pandas operations and visualization standards
- Provide dataset and high-level analysis goals
- AI creates analysis plan with specific questions
- Generate exploratory analysis, statistics, and visualizations

**Example:** `Data_analysis/road_accident_dataset.csv` - accident patterns by country, region, time, severity

### Image Analysis
- Configure `napari-mcp` and `cellpose` servers
- `Image-analysis.mdc` rule activates for `.png` files
- AI uses MCPs for segmentation instead of custom code
- Interactive visualization and quantification

**Example:** `Image_analysis/demo_images/` - 23 microscopy images for cell segmentation

### Scientific Computing
- Use `sympy-mcp` for symbolic math, `fmcp` for plotting
- Domain rules provide physics/math context
- Solve equations symbolically, generate publication-quality plots
- Auto-generate LaTeX equations

## Reference

### Rules

| Rule | Description | When Applied |
|------|-------------|--------------|
| `rules.mdc` | Main rule, domain expertise, data analysis | Always |
| `python-coding-standards.mdc` | Python patterns, Jupyter workflows, plotting | Always |
| `Image-analysis.mdc` | Image analysis, MCP tool prioritization | For `.png` files |
| `project-repo.mdc` | Project structure, file organization | Always |

### MCP Servers

| MCP | Capabilities | Use Cases |
|-----|-------------|-----------|
| `napari-mcp` | Interactive image visualization | Microscopy, 3D imaging, segmentation |
| `cellpose` | Cell segmentation | Cell counting, morphology analysis |
| `fmcp` | Math plotting, numpy, sympy | Scientific plots, numerical computation |
| `sympy-mcp` | Symbolic mathematics | Calculus, algebra, differential equations |
| `claude-scientific-skills` | Scientific computing | Research computations |
| `data-forge` | Data manipulation | Complex data transformations |
| `Notion` | Notion integration | Note-taking, documentation |
| `cursor-ide-browser` | Browser automation | Web testing, scraping |

### Skills

| Skill | Purpose |
|-------|---------|
| `create-rule` | Create new Cursor rules for persistent guidance |
| `create-skill` | Author new agent skills |
| `update-cursor-settings` | Modify Cursor/VS Code settings |

## Customization

### Adapt to Your Research

1. **Replace Data**: Swap `Data_analysis/` and `Image_analysis/` with your datasets
2. **Customize Rules**: Edit `.cursor/rules/` for your domain and coding style
3. **Add MCPs**: Configure additional servers (see [mcpservers.org](https://mcpservers.org))
4. **Create Skills**: Build custom skills for repetitive tasks using `create-skill`
5. **Document Workflows**: Update README with your specific patterns

### Quick Tips

- **Layer context**: General standards → Domain expertise → Project patterns
- **Use conditional rules**: Apply rules based on file type
- **Combine tools**: Rules + MCPs + Skills work together
- **Iterate**: Start minimal, add patterns as you discover them

## Resources

- **Cursor Documentation**: [cursor.sh/docs](https://cursor.sh/docs)
- **Model Context Protocol**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP Servers**: [mcpservers.org](https://mcpservers.org)
- **Cursor Rules**: [cursor.directory](https://cursor.directory)

## License

Copyright © 2024 Suraj Sahu. All rights reserved.

This is a private research repository. All code, data, and documentation are proprietary and must not be shared, published, or made available outside the authorized research group without explicit written permission.

## Contact

**Author:** Suraj Kumar Sahu (ssahu2@ucmerced.edu)

**Institution:** University of California, Merced
