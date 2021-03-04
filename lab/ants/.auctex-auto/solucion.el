(TeX-add-style-hook
 "solucion"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "spanish") ("geometry" "margin=1.5cm") ("biblatex" "style=alphabetic")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "babel"
    "geometry"
    "arev"
    "hyperref"
    "subcaption"
    "amsmath"
    "biblatex"
    "graphicx"
    "verbatimbox"
    "longtable"
    "tikz")
   (TeX-add-symbols
    '("furl" 1))
   (LaTeX-add-labels
    "fig:sch-ui"
    "fig:sim75"
    "fig:sim755"
    "fig:sim-max"
    "fig:state-conv75"
    "fig:chart-conv75"
    "fig:conv75"
    "fig:conv-sim"
    "fig:sche-n500"
    "fig:sche-n5010"
    "fig:sche-n50"
    "fig:sche-smax-min"
    "fig:sche-smax-max"
    "fig:sche-conv3"
    "fig:sche-3-0625"
    "fig:sche-3-06251"
    "fig:sche-3smax"
    "fig:termite-ui"
    "fig:termite-2chips"
    "fig:termite-teleport"
    "fig:ant-ui"
    "fig:ds"
    "fig:ant-chaos"
    "fig:ant-compress"
    "fig:langton-init"
    "fig:langton-nom"
    "tab:langton"
    "fig:langton-ui"
    "fig:langton-150"
    "fig:langton-7"
    "tab:langton-evol"
    "tab:langton-alive"
    "eq:langton-n"
    "eq:langton-a"
    "eq:langton-final")
   (LaTeX-add-bibliographies
    "refs"))
 :latex)

