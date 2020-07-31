import streamlit as st
import pandas as pd
import sys
from collections import defaultdict
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../src')

from src import sce # NOTE: SCE is from https://github.com/KathTheDragon/Conlanger and is by KathTheDragon


def a_page():

    st.title('A -> A1/A2/A3 Derivamatron')

    selected_cols = st.radio('Daughters',['A1', 'A2', 'A3'], index=0)
    show_in = st.checkbox('Show input in output', value=False)
    pos = st.radio('Part of Speech', ['Noun (inan)', 'Noun (anim)', 'Verb', 'Other'], index=3)
    words = []
    if pos == 'Noun (inan)':
        definite = st.checkbox('I-class?', value=False)
        words = st.text_area('Words to derive', value='a,i')
    else:
        words = st.text_area('Words to derive', value='')





    output = []
    ruleset = ""
    affixes = {}
    input = {}

    if pos == 'Noun (inan)':
        words2 = [tuple(w.split(',')) for w in words.split('\n')]
        if definite == True:
            affixes = {'SG':
                {'NOM':'si'
                    , 'NOMPST':'msi'
                    , 'GEN':'sišu'
                    , 'GENPST':'msišu'
                    , 'OBL':'ʔi'
                    , 'OBLPST':'mi'
                }
                , 'PL': {
                    'NOM':'Vt'
                    , 'NOMPST':'pnɨt'
                    , 'GEN':'Vču'
                    , 'GENPST':'pnɨču'
                    , 'OBL':'t'
                    , 'OBLPST':'pti'
                }
            }
        else:
            affixes = {'SG':
                {'NOM':'s'
                    , 'NOMPST':'msu'
                    , 'GEN':'ššu'
                    , 'GENPST':'msušu'
                    , 'OBL':''
                    , 'OBLPST':'m'
                }
                , 'PL': {
                    'NOM':'Vt'
                    , 'NOMPST':'pnɨt'
                    , 'GEN':'Vču'
                    , 'GENPST':'pnɨču'
                    , 'OBL':'t'
                    , 'OBLPST':'pti'
                }
            }
        for sg, pl in words2:
            input[sg+'/'+pl] = {'SG':{}, 'PL':{}}
            for feature, suffix in affixes['SG'].items():
                input[sg+'/'+pl]['SG'][feature] = sg + suffix
            for feature, suffix in affixes['PL'].items():
                input[sg+'/'+pl]['PL'][feature] = pl + suffix
    else:
        words = words.split('\n')

    st.write("## Results in Daughter:")

    # if pos == 'Noun (inan)':
    #     with open('protomorpho/proto_ninan.txt', 'r') as t:
    #         ruleset = t.read()
    #         words = sce.run(words, ruleset, output='list')

    # with open('protomorpho/proto_phono.txt', 'r') as t:
    #     ruleset = t.read()
    #     output = sce.run(words, ruleset, output='list')

    if selected_cols == 'A1':
        open_page = 'a_langs/a1.txt'
    elif selected_cols == 'A2':
        open_page = 'a_langs/a2.txt'
    else:
        open_page = 'a_langs/a3.txt'

    with open(open_page, 'r') as t:
        ruleset = t.read()
        output = {'SG':{}, 'PL':{}}
        if pos == 'Noun (inan)':
            for form in input:
                st.write(form)
                for number in input[form]:
                    for feature in input[form][number]:
                        output[number][feature] = sce.run([input[form][number][feature]], ruleset, output='str')
                output_df = pd.DataFrame(output)
                st.write(output_df)
                output = {'SG':{}, 'PL':{}}

        else:
            output = sce.run(words, ruleset, output='list')

            if show_in:
                output = ['{} \t->\t {}'.format(words[i], o) for i, o in enumerate(output)]
            output = '\n'.join(output)
            st.text(output)

    if st.button('Show SCE rules'):
        st.text(ruleset)
