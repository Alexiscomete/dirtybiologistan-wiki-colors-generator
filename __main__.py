#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import yaml

# Load colors
with open("colors.yml", "r", encoding="utf-8") as f:
    colors = yaml.safe_load(f)

# Load template
with open("css_template.css", "r") as f:
    css_template = f.read()

# Add to output the template with each page value
output = ""
for region in colors:
    # Correctly format the page name; space and / become _
    page_name = region.replace(" ", "_").replace("'", "_").replace("/", "_").strip("_")
    output += css_template.replace("PAGE", page_name).replace("COLOR", colors[region])
    # Do this for each language
    for prefix in ["En", "Es", "Db", "Eo"]:
        output += css_template.replace("PAGE", prefix+"_"+page_name).replace("COLOR", colors[region])

# Minify output
output = output.replace("\n", "").replace(" ", "")

# Write output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(output)