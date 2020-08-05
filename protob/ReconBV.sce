C=m,n,ñ,ŋ,ph,p,b,th,t,d,kwh,kw,gw,kh,k,g,qh,q,tsh,ts,dz,r,rn,l,y,ny,w,mw,ɰ,ŋɰ
V=a,i,u,o
VV=aa,ii,uu,oo
Vstress=á,í,ú,ó
VVstress=áá,íí,úú,óó
VVV=[Vstress],[VVstress]
Vall=[V],[VV],[Vstress],[VVstress]
INFLEX=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
N=m,n,ñ,ŋ
VOICE=ACT,REFL,CAUS
REL=SREL,OREL

//---

Ø > N / _*NPST
Ø > P
-\-

P > nalkk
N > nalkal

//

+a / [C]_[VOICE]REM
+a / [C]_REFL*[REL]
ACTREM > ŋ / _[REL]
ACTREM > ŋg 
CAUSREM > nti / _[REL]
CAUSREM > ny
-PST
-NPST
-ACT
CAUS > :i
: > u: / [C][C]_
: > t / [C]_
[V]: > [VV]
[Vstress]: > [VVstress]
VIS > óyi / i([C])([C])([C])([C])(REFL)(REM)_
VIS > íyi
NVIS > íŋu / u([C])([C])([C])([C])(REFL)(REM)_
NVIS > úŋu
OREL > ndínru / u([C])([C])([C])([C])(REFL)_
OREL > ndúnru
SREL > ndánra
REFLREM > nta
REFL > t / _nd
REFL > tt

//Final Morphopho

[u,i] > [w,y] / _[Vall]
uu,úú,ii,íí > uw,úw,iy,íy / _[Vall]
aa,áá,oo,óo > aɰ,áɰ,ow,ów / _[Vall]
ai, aí > ii, íí
au, aú > oo, óó

---

Ø-ACT-NPST-VIS
Ø-ACT-NPST-NVIS
Ø-ACT-NPST-SREL
Ø-ACT-NPST-OREL
Ø-ACT-PST-VIS
Ø-ACT-PST-NVIS
Ø-ACT-PST-SREL
Ø-ACT-PST-OREL
Ø-ACT-REM-VIS
Ø-ACT-REM-NVIS
Ø-ACT-REM-SREL
Ø-ACT-REM-OREL
Ø-REFL-NPST-VIS
Ø-REFL-NPST-NVIS
Ø-REFL-NPST-SREL
Ø-REFL-NPST-OREL
Ø-REFL-PST-VIS
Ø-REFL-PST-NVIS
Ø-REFL-PST-SREL
Ø-REFL-PST-OREL
Ø-REFL-REM-VIS
Ø-REFL-REM-NVIS
Ø-REFL-REM-SREL
Ø-REFL-REM-OREL
Ø-CAUS-NPST-VIS
Ø-CAUS-NPST-NVIS
Ø-CAUS-NPST-SREL
Ø-CAUS-NPST-OREL
Ø-CAUS-PST-VIS
Ø-CAUS-PST-NVIS
Ø-CAUS-PST-SREL
Ø-CAUS-PST-OREL
Ø-CAUS-REM-VIS
Ø-CAUS-REM-NVIS
Ø-CAUS-REM-SREL
Ø-CAUS-REM-OREL

---

MID
CAUS
ACT
NPST
PST
REM
VIS
NVIS
SREL
OREL
ph
th
kwh
kw
gw
kh
qh
tsh
ts
dz
rn
mw
ŋɰ
aa
ii
uu
oo
áá
íí
úú
óó

---

,