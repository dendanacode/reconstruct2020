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
    if pos == 'Noun (inan)' or pos == 'Noun (anim)':
        definite = st.checkbox('I-class?', value=False)
        if pos == 'Noun (inan)':
            words = st.text_area('Words to derive (comma-separate singular/plural stems)', value='a,i')
        elif pos == 'Noun (anim)':
            words = st.text_area('Words to derive', value='')
    elif pos == 'Verb':
        # verb_class = st.radio('Verb Class', ['H', 'V', 'N'], index=0)
        words = st.text_area('Words to derive (comma-separate pfv/ipfv stems + class [H/V/N])', value='a,i,H')
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
    elif pos == 'Noun (anim)':
        words2 = words.split('\n')
        if definite == False:
            affixes = {'SG':
                {'NOM':''
                    , 'NOMPST':'pɨ'
                    , 'GEN':'nšu'
                    , 'GENPST':'manšu'
                    , 'OBL':'n'
                    , 'OBLPST':'man'
                }
                , 'PL': {
                    'NOM':'m'
                    , 'NOMPST':'mam'
                    , 'GEN':'nsVšu'
                    , 'GENPST':'mansɨšu'
                    , 'OBL':'nsV'
                    , 'OBLPST':'mansɨ'
                }
            }
        else:
            affixes = {'SG':
                {'NOM':'ʔi'
                    , 'NOMPST':'pi'
                    , 'GEN':'nišu'
                    , 'GENPST':'manišu'
                    , 'OBL':'ni'
                    , 'OBLPST':'mani'
                }
                , 'PL': {
                    'NOM':'m'
                    , 'NOMPST':'mam'
                    , 'GEN':'nsVšu'
                    , 'GENPST':'mansɨšu'
                    , 'OBL':'nsV'
                    , 'OBLPST':'mansɨ'
                }
            }
        for stem in words2:
            input[stem] = {'SG':{}, 'PL':{}}
            for feature, suffix in affixes['SG'].items():
                input[stem]['SG'][feature] = stem + suffix
            for feature, suffix in affixes['PL'].items():
                input[stem]['PL'][feature] = stem + suffix

    elif pos == 'Verb':
        words2 = [tuple(w.split(',')) for w in words.split('\n')]
        for stem in words2:
            stem_key = stem[0] + '/' + stem[1]
            if stem[2] == 'H':
                input[stem_key] = {'PFV':stem[0], 'IPFV':stem[1], 'HAB':stem[0] + stem[0]}
            elif stem[2] == 'V' or stem[2] == 'D':
                input[stem_key] = {'PFV':'vA' + stem[0], 'IPFV':'vA' + stem[1], 'HAB':'vA' + stem[0] + stem[0]}
            elif stem[2] == 'N':
                input[stem_key] = {'PFV':'ni' + stem[0], 'IPFV':'ni' + stem[1], 'HAB':'ni' + stem[0] + stem[0]}



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
        if pos == 'Noun (inan)' or pos == 'Noun (anim)':
            output = {'SG':{}, 'PL':{}}
            for form in input:
                st.write(form)
                for number in input[form]:
                    for feature in input[form][number]:
                        output[number][feature] = sce.run([input[form][number][feature]], ruleset, output='str')
                output_df = pd.DataFrame(output)
                st.write(output_df)
                output = {'SG':{}, 'PL':{}}
        elif pos == 'Verb':
            output = {'PFV':'', 'IPFV':'', 'HAB':''}
            for form in input:
                st.write(form)
                for feature in input[form]:
                    output[feature] = sce.run([input[form][feature]], ruleset, output='str')
                output_df = pd.DataFrame(output, index=[0])
                st.write(output_df)
                output = {'PFV':'', 'IPFV':'', 'HAB':''}

        else:
            output = sce.run(words, ruleset, output='list')

            if show_in:
                output = ['{} \t->\t {}'.format(words[i], o) for i, o in enumerate(output)]
            output = '\n'.join(output)
            st.text(output)

    if st.button('Show SCE rules'):
        st.text(ruleset)
