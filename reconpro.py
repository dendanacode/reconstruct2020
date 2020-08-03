import streamlit as st
#import pandas as pd
#from src import sce # NOTE: SCE is from https://github.com/KathTheDragon/Conlanger and is by KathTheDragon
from protomorpho.protomorpho import proto_verb_morpho_page
from protoa.protoa import protoa_page
from a_langs.a import a_page
from protob.protob import protob_page

page = st.selectbox('Page', ['Homepage'
, 'Proto Verb Morpho'
, 'Proto to A derivation'
, 'Proto to B derivation'
, 'A Verb Morpho + Deriv'
, 'B Verb Morpho + Deriv'
, 'A Deriv'
, 'B Deriv'], index=0)

if page == 'Proto Verb Morpho':
    proto_verb_morpho_page()
elif page == 'Proto to A derivation':
    protoa_page()
elif page == 'A Deriv':
    a_page()
elif page == 'Proto to B derivation':
    protob_page()
elif page == 'Homepage':
    st.title('reCONstruct 2020 tools')
    st.write("""
## Welcome to the reCONstruct 2020 tools site!
### The following pages are available for use:
* Proto Verb Morpho - conjugates verbs in the protolanguage
* Proto to A derivation - runs sound changes between proto and A
* Proto to B derivation - runs sound changes between proto and B
* A Deriv - derive words from proto-A to daughters
### The following pages may or may not be built sometime:
* A Verb Morpho + Deriv - conjugates verbs in A and allows you to run your own sound changes on them
* B Verb Morpho + Deriv - same thing but with B
* B Deriv - derive words from languages A or B using your own SCs

-dendana
    """)
else:
    st.title('reCONstruct 2020 tools')
    st.write("""
# Oops!
I haven't made this page yet.

    """)
