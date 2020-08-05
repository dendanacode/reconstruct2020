import streamlit as st
import pandas as pd
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../src')

from src import sce # NOTE: SCE is from https://github.com/KathTheDragon/Conlanger and is by KathTheDragon


def protob_page():

    st.title('proto -> B Derivamatron')

    show_in = st.checkbox('Show input in output', value=False)
    pos = st.radio('Part of Speech', ['Noun (inan)', 'Noun (anim)', 'Verb', 'Other'])

    words = st.text_area('Words to derive', value='')
    output = []
    ruleset = ""
    words = words.split('\n')

    st.write("## Results in B:")

    # if pos == 'Noun (inan)':
    #     with open('protomorpho/proto_ninan.txt', 'r') as t:
    #         ruleset = t.read()
    #         words = sce.run(words, ruleset, output='list')

    if pos == 'Noun (anim)':
        temp_words = []
        for word in words:
            temp_words.append(word)
            temp_words.append(word + 'ni')
            temp_words.append(word + 'ns')
            temp_words.append(word + 'bansi')
            temp_words.append('')
        words = temp_words

    elif pos == 'Noun (inan)':
        temp_words = []
        for word in words:
            temp_words.append(word + 'usi')
            temp_words.append(word + 'ubsi')
            temp_words.append(word + 'ibnut')
            temp_words.append('')
        words = temp_words
        with open('protob/proto_morpho_b.txt', 'r') as t:
            ruleset = t.read()
            words = sce.run(words, ruleset, output='list')

    elif pos == 'Verb':
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

def protob_morpho_page():
    st.title('proto -> B Derivamatron')

    show_in = st.checkbox('Show Proto-B input', value=False)
    pos = st.radio('Part of Speech', ['Noun (inan)', 'Noun (anim)', 'Verb', 'Other'])

    words = st.text_area('Words to derive (comma-separated stems)', value='kambúúŋa,kamwutsŋgá,kamwuuŋu')

    if pos == 'Noun (anim)':
        features = {'visibility':['VIS', 'NVIS']
            , 'number':['SG', 'PL']
            , 'case': ['DIR', 'OBL']
            , 'definite': ['NDEF', 'DEF']}
        sets = [[]]

        for feature, values in features.items():
            for i in range(len(sets)):
                st0 = sets.pop(0)
                for value in values:
                    set_copy = st0.copy()
                    set_copy.append(value)
                    sets.append(set_copy)
        output = []
        schema = ['word']
        schema.extend([feature for feature in features])
        #schema.append('gloss')
        schema.append('form')
        with open('protob/ReconBAnN.sce', 'r') as t:
            ruleset = t.read()
            for word in words.split('\n'):
                w_out = []
                for set in sets:
                    line = [word]
                    line.extend(set)
                    gloss = word.replace(',', '¶').replace('¶', '•', 1) + 'ð' + 'ð'.join(set)
                    #line.append(gloss)
                    line.append(sce.run([gloss], ruleset, output='str'))
                    w_out.append(line)
                output.append(w_out)


        for w in output:
            df = pd.DataFrame(w, columns =schema)
            st.write(df)





    # Ø-VIS-SG-DIR-NDEF
    # Ø-VIS-SG-DIR-DEF
    # Ø-VIS-SG-OBL-NDEF
    # Ø-VIS-SG-OBL-DEF
    # Ø-VIS-PL-DIR-NDEF
    # Ø-VIS-PL-DIR-DEF
    # Ø-VIS-PL-OBL-NDEF
    # Ø-VIS-PL-OBL-DEF
    # Ø-NVIS-SG-DIR-NDEF
    # Ø-NVIS-SG-DIR-DEF
    # Ø-NVIS-SG-OBL-NDEF
    # Ø-NVIS-SG-OBL-DEF
    # Ø-NVIS-PL-DIR-NDEF
    # Ø-NVIS-PL-DIR-DEF
    # Ø-NVIS-PL-OBL-NDEF
    # Ø-NVIS-PL-OBL-DEF
