import streamlit as st
import pandas as pd
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../src')

from src import sce # NOTE: SCE is from https://github.com/KathTheDragon/Conlanger and is by KathTheDragon


def proto_verb_morpho_page():

    st.title('proto-reCONstruct 2020 Verbamatron')

    features = {
    'Mood': ['frustrative', 'accidental', 'opt', 'adm', 'hort', 'proh', 'decl']
    , 'Thematic': ['nullthem', 'nithem', 'dthem']
    , 'Evidential': ['nullevid', 'conjunct']
    , 'Animacy': ['anim', 'inan']
    # , 'Transitivity': ['tr']
    , 'STEM': ['STEM']
    , 'Aspect': ['ipfv', 'pfv']
    , 'Voice': ['unmarkedvoice', 'middle', 'caus']
    , 'Aspect_2': ['dur', 'pstpfv', 'unmarkedaspect']
    , 'Spatial': ['here', 'there', 'overthere', 'nullspatial']
    , 'Question': ['question', 'nullquestion']

    # , 'dynamic': ['static', 'dynamic']
    }

    stem = st.text_input('Target Stem(s), comma-separated', value='musa')
    stems = stem.split(',')

    feature_selections = {}
    for feature, values in features.items():
        if feature != 'STEM':
            if values != []:
                feature_selections[feature] = st.sidebar.multiselect('{} Features'.format(feature), values, [values[0]])
        elif feature == 'STEM':
            feature_selections[feature] = ['STEM']

    cols = []
    cols.extend([k for k in features.keys()])
    cols.remove('STEM')

    cols.extend(['Stem', 'Features', 'Morphemes', 'Phonemes', 'Word'])
    selected_cols = st.sidebar.multiselect('Search Columns',cols, cols)

    sets = [[]]

    for feature, values in feature_selections.items():
        for i in range(len(sets)):
            st0 = sets.pop(0)
            for value in values:
                set_copy = st0.copy()
                set_copy.append(value)
                sets.append(set_copy)
    #print(sets)
    sets_str = {s:[] for s in stems}
    step1 = {s:[] for s in stems}
    step2 = {s:[] for s in stems}
    output = {s:[] for s in stems}

    # limit the number of sets (may have to move this to the set generation part)

    for s in stems:
        for l in sets:
            if not (('opt' in l or 'adm' in l or 'hort' in l or 'proh' in l) and ('ipfv' in l or 'conjunct' in l or 'dur' in l or 'pstpfv' in l or 'question' in l)):
                if not ('pfv' in l and 'dur' in l):
                    if not ('ipfv' in l and 'pstpfv' in l):
                        stem_representation = ''
                        for i, value in enumerate(l):
                            if value == 'STEM':
                                stem_representation += '{}£'.format(s)
                            elif i == 0:
                                stem_representation += '{}§'.format(value)
                            elif i == len(l) - 1:
                                stem_representation += '{}'.format(value)
                            else:
                                stem_representation += '{}§'.format(value)
                        sets_str[s].append(stem_representation)

    with open('protomorpho/proto_morpho.txt', 'r') as t:
        ruleset = t.read()
        for s in stems:
            #print(sets_str[s])
            step1[s] = sce.run(sets_str[s], ruleset, output='list')
            #step1[s] = [x.replace('incorporate', '¶').replace('null', '') for x in ls]

    with open('protomorpho/proto_morph_phon.txt', 'r') as t:
        ruleset = t.read()
        for s in stems:
            step2[s] = sce.run(step1[s], ruleset, output='list')
            #step2[s] = [x.replace('¶', incorporate_2) for x in ls]

    with open('protomorpho/proto_phono.txt', 'r') as t:
        ruleset = t.read()
        for s in stems:
            output[s] = sce.run(step2[s], ruleset, output='list')

    unique = {}
    out = []
    for s in stems:
        for i, word in enumerate(step1[s]):
            #print('{} : {}'.format(i, word))
            features_str = sets_str[s][i].replace('§', '.').replace('£', '.')
            #st.write(features_str)
            features_str = features_str.replace('{}.'.format(s), '')
            features_list = features_str.split('.')
            #st.write(features_list)
            word_str = word.replace('§', '.').replace('£', '.')
            phoneme_str = step2[s][i].replace('§', '.').replace('£', '')
            features_list.extend([s, features_str, word_str, phoneme_str, output[s][i]])
            #print(features_list)
            out.append(features_list)
            #print(features_list)
            #print("{} \n\t > {} \n\t > {} \n\t > {}".format(features_str, word_str, phoneme_str, output[s][i]))
        unique[s] = set(output[s])

    #print(out)

    pandas_forms = pd.DataFrame(out, columns=cols)

    for s in stems:
        st.markdown("Number of forms from stem {}: {}".format(s, len(output[s])))
        st.markdown("Number of unique forms from stem {}: {}".format(s, len(unique[s])))
    for s in stems:
        st.write(pandas_forms.loc[pandas_forms['Stem'] == s][selected_cols])
