C=m,n,ŋ,b,d,t,k,p,q,s,ł,l,h,kʷ
stop=b,d,t,k,p,q,kʷ
nasal=m,n,ŋ
P=p,t,k,kʷ,q
Ph=pʰ,tʰ,kʰ,kʰʷ,qʰ
V=a,i,u
stress=á,í,ú
VV=[V],[stress]

// just so this doesn't come back to haunt me later
p > kʷ

// 1. Proto allophony
+a / [C]_q[C]
dd > t
dh > t
+u / [C][C]_[C]
[stop] > h / _[stop]#

// 2. Epenthesis
// a
+ i / #[t,d,s,ł,l]_[[P], [nasal]], #[t,d,s,ł,l]_[C][C], #([C])[t,d,s,ł,l,n]_#
// b
+ a / #[[stop],l,h]_[[P], [nasal]], #[[stop],l,h]_[C][C], #([C])[C]_#

// 3. Stress
// Marking heavy syllables
+ · / [V][C]_ ! _[V]
// a
[V]@1 > [stress] ! [C]·
// b
- · / _*·
[V] > [stress] / _[C]·
- ·

// 4. Final vowel addition
[VV]@-1 >^ [C]_#
[stress] > [V] / [stress]*_


// 5. Aspiration
[P] > [Ph] / h_, _h
- h / [Ph]_, _[Ph]

// 6. Fortition: when stressed
[P] > [Ph] / #_([C])[stress]
[P] > %% / _[stress] //! [C]_
l > ł / #_([C])[stress]
l > %% / _([C])[stress]
h > p / _ú > k / _á > ts / _í
[b,d,s] > [p,t,ts] / _([C])[stress]
[m,n,ŋ] > [b,d,g] / #_[stress]
[m,n,ŋ] > [mb,nd,ŋg] / _[stress]

P+=ts
Ph+=tsʰ

// 7. Intervocalic lenition (unstressed only)
-h / [VV]_[V]
[b,m,t,d,n,k,ŋ,kʷ,q,s,ł] > [w,w̃,d,ɾ,ɾ̃,g,ɰ̃,gʷ,ŋ,h,ʎ] / [VV]_[V]

// 8. Palatalization
h > s / _í
[l,ł] > ʎ / _[i,í]
ʎ > j
[n,ŋ] > ɲ / _[i,í]
[ɾ̃,ɰ̃] > j̃ / _[i,í]

C+=ts,dz,ɾ,ɾ̃,j,j̃,w,w̃,ɰ̃,ɰ,gʷ,g,ɲ,[Ph]

// 9. Gliding
[i,u] > [j,w] / _[VV] ! [j,w]_

// 10. Vowel harmony (with cons dissimilation)
J=j,j̃,ɲ,s,ts
u,ú > ju,jú / [a,u,á,ú]([C])([C])[k,kʷ,g,gʷ,w,w̃,ɰ,ɰ̃,ŋ]([C])_[C]([C])[i,í]
i,í > u,ú / [a,á,i,í]([C])([C])[J]([C])_[C]([C])[u,ú]
u,ú > a,á / [i,í,u,ú]([C])([C])[k,kʷ,g,gʷ,q]([C])_[C]([C])[a,á]
i,í > o,ó / [i,í,u,ú]([C])([C])[J]([C])_[C]([C])[a,á]

// 11. Vowel disharmony
i,í > o,ó / [i,í][C]([C])([C])_[C]([C])([C])[i,í]
u,ú > i,í / [u,ú][C]([C]([C]))_[C]([C]([C]))[u,ú]
- a / [a,á][C]_[C][a,á]

V+=o
stress+=ó
VV=[V],[stress]

// 12. kill h
Vlong=aa,ii,uu,oo
Vlongs=áá,íí,úú,óó
VVlong=[Vlong],[Vlongs]
VVV=[VV],[VVlong]
graphs+=[VVlong]

[P]h > [Ph]
[VV]h > [VVlong]
- h

s > dz / [VVV]_i
s > n / #_[VVV]
[VV]s > [VVlong] / _[C], _#
s > t / _[VVV]
- s

ł > [] / _# > l

// 13. minor declusterfuck
nɾ > ɾ̃
mw > w̃
ŋɰ > ɰ̃
ɲj > j̃
[n,ŋ] > m / [kʰʷ,kʷ,gʷ]_

t[ɾ,ɾ̃] > d / [VVV]_
k[ɰ,ɰ̃] > g / [VVV]_
kʷ[ɰ,ɰ̃] > gʷ / [VVV]_
p[w,w̃] > b / [VVV]_
qɰ̃ > ŋ / [VVV]_
-ɰ / q_[VVV]
ts[j,j̃] > dz / [VVV]_
[Ph][ɾ̃,j̃,w̃,ɰ̃] > [P][n,ɲ,m,ŋ]
kq > qq
qk > kk
kʷk > kk
kkʷ > kʷkʷ
kʷq > qq
qkʷ > qq
pkʷ > pp
kʷp > pp

B=b,d,g,gʷ,dz
stop+=[P],[Ph],[B]

[VV][B] > [VVlong] / _[stop]
+i / #[C]_[C][C], #[[stop],l]_[[stop],l]
l > u / #_[C]

// 14. One more vowel round

[u,i] > [w,j] / [VVV]_[VVV]
uu,úú,ii,íí > uw,úw,ij,íj / _[VVV]
aa,áá > aɰ,áɰ / _[VVV]
ai, aí > ii, íí
au, aú > oo, óó
i,a > ɨ,ə / [VVV]([C])([C])[C]_#
oo,óó > uu,úú / _#
áa,aá > áá
íi,ií > íí
óo,oó > óó
úu,uú > úú
