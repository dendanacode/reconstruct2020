import streamlit as st
import pandas as pd
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../src')

from src import sce # NOTE: SCE is from https://github.com/KathTheDragon/Conlanger and is by KathTheDragon


def protob_page():

    st.title('proto -> B Derivamatron')

    show_in = st.checkbox('Show input in output', value=False)
    pos = st.radio('Part of Speech', [# 'Noun (inan)', 'Noun (anim)',
     'Verb', 'Other'])

    words = st.text_area('Words to derive', value='')
    output = []
    ruleset = ""
    words = words.split('\n')

    st.write("## Results in B:")

    # if pos == 'Noun (inan)':
    #     with open('protomorpho/proto_ninan.txt', 'r') as t:
    #         ruleset = t.read()
    #         words = sce.run(words, ruleset, output='list')

    if pos == 'Verb':
        temp_words = []
        for word in words:
            temp_words.append(word)
            temp_words.append(word + '£IL')
            temp_words.append(word + '£QU')
            temp_words.append(word + '£CV§IL')
            temp_words.append(word + '£CV§QU')
            temp_words.append(word + '£CV§KWA§GK')
            temp_words.append(word + '£CV§HTA§GK')
            temp_words.append(word + '£CV§SKI§GK')
            temp_words.append('')
        words = temp_words
        with open('protob/proto_morpho_b.txt', 'r') as t:
            ruleset = t.read()
            words = sce.run(words, ruleset, output='list')

    with open('protomorpho/proto_phono.txt', 'r') as t:
        ruleset = t.read()
        words = sce.run(words, ruleset, output='list')

    with open('protob/ReconB_3.sce', 'r') as t:
        ruleset = t.read()
        output = sce.run(words, ruleset, output='list')

    if show_in:
        output = ['{} \t->\t {}'.format(words[i], o) for i, o in enumerate(output)]
    output = '\n'.join(output)
    st.text(output)

    if st.button('Show SCE rules'):
        st.text(ruleset)
