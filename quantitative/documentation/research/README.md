# Research

## LaTeX Setup

The following configuration can be added to the VS Code `settings.json` file to streamline the LaTeX document compilation process. This setup uses `latexmk` for building the documents and ensures that the output PDF is copied to the main directory (i.e. where the `.tex` file is) for easy access.

The [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension for VSCode must be installed to utilise this configuration.

```json
{
  "[latex]": {
    "editor.defaultFormatter": "James-Yu.latex-workshop",
    "editor.formatOnSave": true
  },
  "[bibtex]": {
    "editor.defaultFormatter": "James-Yu.latex-workshop",
    "editor.formatOnSave": true
  },
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.latex.outDir": "%DIR%/out",
  "latex-workshop.latex.tools": [
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "-outdir=%DIR%/out",
        "%DOC%"
      ],
      "env": {}
    },
    {
      "name": "copy_pdf",
      "command": "cp",
      "args": ["%DIR%/out/%DOCFILE%.pdf", "%DIR%/%DOCFILE%.pdf"]
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "latexmk 🔃",
      "tools": ["latexmk", "copy_pdf"]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab",
  "latex-workshop.formatting.latex": "latexindent",
  "latex-workshop.formatting.latexindent.path": "latexindent",
  "latex-workshop.formatting.latexindent.args": [
    "-c",
    "/tmp/",
    "%TMPFILE%"
  ]
}
```
