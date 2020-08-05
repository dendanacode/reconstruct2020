C=m,n,ñ,ŋ,ph,p,b,th,t,d,kwh,kw,gw,kh,k,g,qh,q,tsh,ts,dz,r,rn,l,y,ny,w,mw,ɰ,ŋɰ
V=a,i,u,o
VV=aa,ii,uu,oo
Vstress=á,í,ú,ó
VVstress=áá,íí,úú,óó
U=u,ú
I=i,í
VVV=[Vstress],[VVstress]
Vall=[V],[VV],[Vstress],[VVstress]
sound=[C],[Vall]
INFLEX=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
graphs=.,ph,th,kwh,kw,gw,kh,qh,tsh,ts,dz,rn,mw,ŋɰ,aa,ii,oo,uu,áá,íí,úú,óó,10,11,12,13,14,15,16


NVISðSGðDIRðNDEF > 9
NVISðSGðDIRðDEF > 10
NVISðSGðOBLðNDEF > 11
NVISðSGðOBLðDEF > 12
NVISðPLðDIRðNDEF > 13
NVISðPLðDIRðDEF > 14
NVISðPLðOBLðNDEF > 15
NVISðPLðOBLðDEF > 16
VISðSGðDIRðNDEF > 1
VISðSGðDIRðDEF > 2
VISðSGðOBLðNDEF > 3
VISðSGðOBLðDEF > 4
VISðPLðDIRðNDEF > 5
VISðPLðDIRðDEF > 6
VISðPLðOBLðNDEF > 7
VISðPLðOBLðDEF > 8


//---

+L / _[1,2,4,6,9,10,12,14]
+U / _[11,13,15,16]
+R / _[3,5,7,8]
-ð


-•*L
-*• / #_*R
-¶*R
-*¶ / #_*U
-U


// L > thímwo
// R > timbí
// U > timwi

//VIS-SG-DIR DEF and NDEF

-1
[VV]2 > [V]ii
2 > i / [VVV]_
[Vall]2 > ii

//Echo vowel ones and 4
4 > nyi

[Vall]@-1 >^ [3,5,7]_
[VVstress],[Vstress] > [V] / [INFLEX]_
3,5,7 > nr,mw,nt
6,8 > mwi,nti
9,10,11,12 > wa,wii,pánra,wanyi
13,14,15,16 > pámwa,wamwi,pánta,pánti

//Final Morphopho

uu,úú,ii,íí > uw,úw,iy,íy / _[Vall]
u > w / _[Vall] ! _[U]
i > y / _[Vall] ! _[I]
aa,áá,oo,óo > aɰ,áɰ,ow,ów / _[Vall]
ai, aí > ii, íí
au, aú > oo, óó
