import streamlit as st
import pandas as pd
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../src')

from src import sce # NOTE: SCE is from https://github.com/KathTheDragon/Conlanger and is by KathTheDragon

sample_daughter = """
C=m,n,ñ,ŋ,ph,p,b,th,t,d,kwh,kw,gw,kh,k,g,qh,q,tsh,ts,dz,r,nr,l,y,ny,w,mw,ɰ,ŋɰ
V=a,i,u,o
VV=aa,ii,uu,oo
Vstress=á,í,ú,ó
VVstress=áá,íí,úú,óó
VVV=[Vstress],[VVstress]
Vall=[V],[VV],[Vstress],[VVstress]
graphs=.,ph,th,kwh,kw,gw,kh,qh,tsh,ts,dz,nr,ny,mw,ŋɰ,ii,íí,uu,úú,oo,óó,aa,áá

a,i > ə,ɨ / [Vall]*_#

-ə

//Nasal → nasal glide

m,n,ñ,ŋ > mw,nr,ny,ŋɰ

- y,w,y,ɰ ! #_

ph,th,kh,kwh,qh,tsh > pp,tt,kk,kkw,qq,tts
ts,dz > tt / [Vall]_[Vall]
ts,dz > t

B=b,d,gw,g,dz
P=p,t,kw,k,ts,q

b,gw > w / _#
g > y / [i,e]_# > w / _#
d > r / _#
dz > y / _#

[B] > :[P] / _[Vall] ! #_
b,gw > : / [o,u]_
d,g,q > : / [i,a]_
[C]: > <
[C]: > <
[V]: > [VV]
[Vstress]: > [VVstress]
-:

[P] > k / _g
[P] > p / _b
[P] > t / _d
[P] > kw / _gw
[B] > [P] / [P]_
kwkw > kkw

ə,ɨ > e
u > o
a > e
íe,áe,óe > é,éé,éé
V+=e
VV+=ee
Vstress+=é
VVstress+=éé
VVV=[Vstress],[VVstress]
Vall=[V],[VV],[Vstress],[VVstress]

graphs+=ee,éé,pp,tt,kk,kkw,qq
C+=qq,pp,tt,kk,kkw,tts,ŋw
q.q,p.p,t.t,k.k,k.kw,t.ts>qq,pp,tt,kk,kkw,tts

+o / [C][C]_[C]
+o / #[C]_[C]

e@2 > o / _*[e,ee,é,éé]

aa > a
[V]o > aa
[V]oo > aa

[VV] > [V] / [V]_, _[V], [Vstress]_
+ʔ / [VVstress]_, [VV]_ ! _[C], _#
+ʔ / _[VVstress], _[VV] ! [C]_, #_

ii > i
i.i > ii
ei > ii
ie > ii
íe,eí > íí
eé,ée > éé
uo > uu
ou > oo
úo,oú > úú
óu,uó > óó
áo,oá > óó

N=m,n,ŋ,ŋw,ñ
[B] > [N] / _
NA=mw,nr,ŋw,ŋɰ,ny
[NA][NA] > [N]

[kw,kkw,ŋw] > [k,kk,ŋ]

r,nr > l / #_[o,ó,oo,óó,u,ú,uu,úú,a,áá,aa,á], [o,ó,oo,óó,u,ú,uu,úú,a,áá,aa,á]_# > y / #_[e,ee,éé,é,i,ii,í,íí], [e,ee,éé,é,i,ii,í,íí]_# > ʔ / [Vall]_[Vall]
-r,nr
ŋɰ,ɰ > mw,w
[NA] > ʔ / _[C], _#
-y / _[i,íí,í,ii]
-w / _[u,úú,ú,uu]

qq > :ʔ
q > ʔ

[V]: > [VV]
[Vstress]: > [VVstress]
-:

//-[V]ʔ

"""

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

    daughter = st.text_area('SCE Rules (define graphs as final category)', value=sample_daughter)

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
        schema.append('daughter')
        with open('protob/ReconBAnN.sce', 'r') as t:
            ruleset = t.read()
            for word in words.split('\n'):
                w_out = []
                for set in sets:
                    line = [word]
                    line.extend(set)
                    gloss = word.replace(',', '¶').replace('¶', '•', 1) + 'ð' + 'ð'.join(set)
                    #line.append(gloss)
                    form = sce.run([gloss], ruleset, output='str')
                    line.append(form)
                    line.append(sce.run([form], daughter, output='str'))
                    w_out.append(line)
                output.append(w_out)


        for w in output:
            st.write('## ' + w[0][0].split(',')[0])
            df = pd.DataFrame(w, columns =schema).drop('word', axis=1)#.drop('number', axis=1).drop('case', axis=1)
            df["vis+num"] = df['visibility'] + '\t' + df['number']
            df["case+def"] = df['case'] + '\t' + df['definite']
            df0 = df.pivot(index='vis+num', columns='case+def', values='form')
            df_d = df.pivot(index='vis+num', columns='case+def', values='daughter')
            df0 = df0.iloc[::-1]
            df_d = df_d.iloc[::-1]
            st.write(df0)
            st.write("Daughter:")
            st.write(df_d)





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
