# Citation Styles Guide

## APS Numbered Style

Physics journals use numbered citations in square brackets.

### In-Text Format

```
Several studies have demonstrated this effect [1].
The results were reported by Doha et al. [2], and later confirmed [3,4].
As shown by previous work [5-8], the transition is sharp.
```

### LaTeX Usage

Use `revtex4-2` document class with `\cite{}` commands:

```latex
\documentclass[aps,prl,twocolumn]{revtex4-2}

% In text:
Several studies have demonstrated this effect~\cite{Smith2020}.
The results were reported by Doha \textit{et al.}~\cite{Doha2022}.
As confirmed by multiple groups~\cite{Peng2025,Zakharov2021}.

% At end of document:
\bibliography{references}
```

### Bibliography File

BibTeX file location:
`Percolation-Driven Compaction of Cell-Matrix Networks/paper/references.bib`

### Best Practices

- Use `~\cite{}` (non-breaking space) to prevent line breaks before citations
- Cite specific figures or equations when referencing others' work: "as shown in Fig. 2 of Ref. [2]"
- Group multiple citations in one bracket: `[3,4]` or `[5-8]`, not `[3][4]`
- Place citations at the end of the clause, before the period
- Use "Ref. [1]" or "Refs. [1,2]" when the citation is the grammatical subject
