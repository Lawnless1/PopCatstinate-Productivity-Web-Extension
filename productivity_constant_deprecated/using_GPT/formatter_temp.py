import re

with open("top_300_website_productivity_score.txt", "r") as file:
    past_file = file.read()

new_excerpt = re.sub(r'(\d+\.\d*\s*\,?\s*)(?:\n|$)', r'\1,\n', past_file)

with open("reformatted_top_300gpt4_700gpt3", "a+") as file:
    file.write(new_excerpt)