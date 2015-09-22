#!/bin/sh

py_files=$(find -name "*.py" | grep -v libs)
if [[ $py_files ]]
then
    total=$(wc -l $py_files | grep total)
    if [[ $total ]]
    then
        py=$(wc -l $py_files | grep total | sed "s|\([0-9]*\) total|\1|")
    else
        py=$(wc -l $py_files | sed "s|\([0-9]*\) .*|\1|")
    fi

else
    py=0
fi

pt_files=$(find -name "*.pt" | grep -v libs)
if [[ $pt_files ]]
then
    total=$(wc -l $pt_files | grep total)
    if [[ $total ]]
    then
        pt=$(wc -l $pt_files | grep total | sed "s|\([0-9]*\) total|\1|")
    else
        pt=$(wc -l $pt_files | sed "s|\([0-9]*\) .*|\1|")
    fi
else
    pt=0
fi

css_files=$(find -name "*.css" | grep -v bootstrap)
if [[ "$css_files" ]]
then
    total=$(wc -l $css_files | grep total)
    if [[ $total ]]
    then
        css=$(wc -l $css_files | grep total | sed "s|\([0-9]*\) total|\1|")
    else
        css=$(wc -l $css_files | sed "s|\([0-9]*\) .*|\1|")
    fi
else
    css=0
fi

js_files=$(find -name "*.js" | grep -v bootstrap)
if [ "$js_files" ]
then
    total=$(wc -l $js_files | grep total)
    if [[ $total ]]
    then
	    js=$(wc -l $js_files | grep total | sed "s|\([0-9]*\) total|\1|")
    else
        js=$(wc -l $js_files | sed "s|\([0-9]*\) .*|\1|")
    fi
else
	js=0
fi

echo Lines: python $py, templates $pt, css $css, javascript $js
echo Total: $(echo $py + $pt + $css + $js | bc)
