# TikZ Patterns — Publication Stage (LaTeX)

## Document setup

```latex
\documentclass[tikz, border=12pt]{standalone}
\usepackage{tikz}
\usepackage{amsmath, amssymb}
\usetikzlibrary{
  arrows.meta, shapes.geometric, positioning,
  calc, backgrounds, fit, decorations.pathreplacing
}
```

## Reusable tikzset styles

```latex
\tikzset{
  cellnode/.style={
    ellipse, draw=#1!70!black, fill=#1!25, thick,
    minimum width=2.4cm, minimum height=1.9cm
  },
  roundbox/.style={
    rounded corners=7pt,
    draw=#1!70!black, fill=#1!18, thick,
    minimum width=4.0cm, minimum height=1.1cm,
    align=center, font=\small\bfseries
  },
  annobox/.style={
    rounded corners=4pt,
    draw=#1!60!black, fill=#1!15,
    inner sep=4pt, align=center, font=\scriptsize
  },
  myarrow/.style={->, >=Stealth, thick, #1},
  dasharrow/.style={->, >=Stealth, thick, dashed, #1},
}
```

## Background panel

```latex
\fill[blue!5, rounded corners=14pt] (-2.5,-4.2) rectangle (13.5,5.8);
```

## Cell nodes

```latex
% Source cell
\node[cellnode=orange, minimum width=1.8cm, minimum height=1.8cm,
      font=\small\bfseries, align=center, text=orange!30!black]
  (source) at (9.0, 0.5) {Source\\(VEGF)};

% Sensing cell
\node[cellnode=cyan!80!blue, font=\normalsize\bfseries, text=blue!40!black]
  (cell) at (0.5, 0.5) {Cell $i$};
```

## Concentration gradient halo

```latex
\foreach \r/\op in {4.2/4, 3.4/7, 2.6/12, 1.8/18, 1.0/28}{
  \fill[orange!50, opacity=0.0\op]
    (9.0, 0.5) ellipse ({\r*1.1} and {\r*0.75});
}
```

## Receptors (small rectangles on cell edge)

```latex
\foreach \dy in {0.35, 0.0, -0.35}{
  \fill[red!65, rounded corners=1.5pt]
    ($(cell.east)+(0.05,\dy)$) rectangle ++(0.40, 0.22);
}
```

## Arrows with annotations

```latex
% Solid arrow with midway annotation box
\draw[myarrow=violet!70!black, line width=1.5pt]
  (reclabel.south) .. controls ++(0.0,-0.9) and ++(0.0, 0.9) ..
  (cascade.north west)
  node[midway, annobox=violet, right=0.05cm] {GPCR / RTK\\signal};

% Dashed arrow
\draw[dasharrow=orange!70!black, line width=1.2pt]
  (gradlabel.south east) to[bend right=15]
  node[midway, above right, font=\scriptsize] {increasing $C$}
  ($(source.north west)+(0.3,0.3)$);
```

## Math in equation footer

```latex
\node[draw=gray!50, fill=white, thick, rounded corners=6pt,
      font=\normalsize, align=center,
      minimum width=15.0cm, minimum height=1.1cm]
  at (5.5, -3.8)
  {$\theta_i(t+1) \;=\;
    \Bigl[\,\theta_i(t) + \eta_i
          + \kappa\,\sin\!\bigl(\phi_{\nabla C_i} - \theta_i\bigr)
    \,\Bigr] \bmod 2\pi$};
```

## Sensing radius

```latex
\draw[draw=blue!50, dashed, thick, opacity=0.55]
  (cell.center) circle (2.9cm);
\node[font=\scriptsize\itshape, text=blue!60, below=2.0cm of cell]
  {$r_c = 3.0$ (sensing radius)};
```

## Compile

```bash
pdflatex -interaction=nonstopmode schematic.tex
```
