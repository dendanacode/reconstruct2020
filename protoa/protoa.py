import streamlit as st
import pandas as pd
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../src')

from src import sce # NOTE: SCE is from https://github.com/KathTheDragon/Conlanger and is by KathTheDragon


def protoa_page():

    st.title('proto -> A Derivamatron')

    show_in = st.checkbox('Show input in output', value=False)
    pos = st.radio('Part of Speech', ['Noun (inan)', 'Noun (anim)', 'Verb (inan)', 'Verb (anim)', 'Other'], index=4)

    words = st.text_area('Words to derive', value='')
    output = []
    ruleset = ""
    words = words.split('\n')

    st.write("## Results in A:")

    # if pos == 'Noun (inan)':
    #     with open('protomorpho/proto_ninan.txt', 'r') as t:
    #         ruleset = t.read()
    #         words = sce.run(words, ruleset, output='list')

    with open('protomorpho/proto_phono.txt', 'r') as t:
        ruleset = t.read()
        output = sce.run(words, ruleset, output='list')

    with open('protoa/proto_to_a.txt', 'r') as t:
        ruleset = t.read()
        output = sce.run(words, ruleset, output='list')

    if show_in:
        output = ['{} \t->\t {}'.format(words[i], o) for i, o in enumerate(output)]
    output = '\n'.join(output)
    st.text(output)

    if st.button('Show SCE rules'):
        st.text(ruleset)
