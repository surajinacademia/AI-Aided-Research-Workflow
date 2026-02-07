# Literature Review Workflow for Claude Code

This workflow enables comprehensive literature research using Claude Code's built-in `general-purpose` agent.

## When to Use

**IMMEDIATELY invoke when user asks about:**
1. Mechanisms or findings from research papers
2. Citations or literature references
3. "How does [X] work" in biological/physical systems
4. Experimental methods or measurements
5. Equations or mathematical models from literature
6. Topics: cell adhesion, actomyosin, RhoA, E-cadherin, cortical flows, myosin
7. ODEs/PDEs in biological modeling
8. "What does the literature say about..."

**DO NOT answer from memory. ALWAYS delegate to the general-purpose agent.**

## How to Invoke

Use the `Task` tool with `subagent_type="general-purpose"`:

```
Task(
  subagent_type="general-purpose",
  description="Literature search",
  prompt="You are an expert literature research specialist in theoretical physics,
          experimental biophysics, bioengineering and computational biology.

          Search for information about: [USER'S QUESTION]

          Follow this systematic search strategy:

          1. Search local literature in the 'literature/' folder using Grep and Read
          2. Search project documentation (Notes.md, module docs) using Grep
          3. If available, search Zotero library using MCP tools:
             - zotero_semantic_search (limit: 10)
             - zotero_get_item_fulltext (for full text)
             - zotero_search_notes (for annotations)
          4. Use web search for recent papers or to fill gaps

          Structure your answer as:
          1. Direct Answer - Clear, concise response
          2. Detailed Explanation - Biological/physical context and mechanisms
          3. Evidence from Literature - Specific findings with citations
          4. Cross-Paper Synthesis - How sources relate/differ
          5. Key Equations/Methods - Mathematical expressions or approaches
          6. Further Reading - Specific files or papers

          Citation format:
          - In-text: Author et al. (Year) found that...
          - With title: Arslan et al. (2024) \"Adhesion-induced cortical flows...\"
          - File ref: See literature/Arslan et al. - 2024 - Adhesion-induced...md
          - Quotes: > \"Quote text\" - Author et al. (Year)

          Quality standards:
          - Comprehensive: Search all sources systematically
          - Specific: Include details, numbers, measurements
          - Critical: Note disagreements or limited evidence
          - Contextual: Explain biological significance
          - Precise: Distinguish observations from predictions"
)
```

## Search Strategy

The agent will follow this systematic approach:

### 1. Parse the Query
- Identify key concepts and extract search terms with synonyms
- Determine information type needed (mechanism, measurement, equation, method)

### 2. Search Local Literature (`literature/` folder)
Use Grep with targeted queries:
```bash
grep -r "keyword" literature/*.md
```
- Start broad to find relevant papers, then drill down for specifics
- Key papers include: Arslan et al. 2024, Bailles et al. 2022, Hannezo et al. 2015

### 3. Search Project Documentation
Use Grep across project `.md` files:
- `Notes.md` - Research notes and derivations
- Module docs - Model implementations

### 4. Search Zotero Library (if MCP available)
Use MCP server `user-zotero`:
- `zotero_semantic_search` - Search library with semantic query
- `zotero_get_item_fulltext` - Get full text using item_key
- `zotero_search_notes` - Search notes and annotations

### 5. Web Search (if gaps remain)
Use WebFetch for recent papers, methods, or verification

## Example Usage

**User asks:** "How does E-cadherin suppress RhoA activity?"

**You invoke:**
```
Task(
  subagent_type="general-purpose",
  description="Literature search: E-cadherin RhoA suppression",
  prompt="[Full prompt template above with user's question inserted]"
)
```

**Agent will:**
1. Parse: E-cadherin, RhoA suppression, mechanochemical coupling
2. Search: Local literature → Project docs → Zotero → Web
3. Synthesize: Compile findings, explain pathway, cite sources

## Quick Reference

**Trigger phrases that require delegation:**
- "How does X work"
- "What is the mechanism"
- "What does the literature say"
- "According to papers"
- "Research shows"
- "Experimental measurements"
- "Mathematical model/equation from literature"

**Key local resources:**
- `literature/` folder - Markdown versions of research papers
- `Notes.md` - Project research notes
- Module documentation files
- Zotero library (via MCP if configured)

## Output Format Requirements

The agent should structure findings as:

**1. Direct Answer** (2-3 sentences)

**2. Detailed Explanation** (biological/physical context)

**3. Evidence from Literature**
- Citation 1: Finding with reference
- Citation 2: Finding with reference
- Citation 3: Finding with reference

**4. Cross-Paper Synthesis** (how sources agree/differ)

**5. Key Equations/Methods** (if applicable)
```
dX/dt = f(X, parameters)
```

**6. Further Reading**
- `literature/Paper1.md`
- `literature/Paper2.md`

## Notes for Claude Code Users

- This workflow uses the `general-purpose` agent, not a custom agent type
- The prompt is comprehensive to ensure systematic searching
- Always delegate literature questions; don't answer from memory
- Agent has access to all file reading and search tools
- Results are returned in a single comprehensive response
