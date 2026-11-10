import pandas as pd,numpy as np,json,sys
D=sys.argv[1]
e=pd.read_csv(f'{D}/ecommerce_provinsi.csv');p=pd.read_csv(f'{D}/penduduk_provinsi.csv');i=pd.read_csv(f'{D}/internet_provinsi.csv')
d=e[e.tahun_data==2024].merge(p[p.tahun==2024],on='provinsi').merge(i[i.tahun==2024],on='provinsi')
d['per1000']=d.jumlah_usaha/d.penduduk*1000
d['share']=d.jumlah_usaha/d.jumlah_usaha.sum()*100
r=np.corrcoef(d.internet_total,d.per1000)[0,1]
rs=d[['internet_total','per1000']].corr(method='spearman').iloc[0,1]
mi,me=d.internet_total.median(),d.per1000.median()
def q(x):
  if x.internet_total>=mi and x.per1000>=me: return 'Siap'
  if x.internet_total>=mi: return 'Potensial'
  if x.per1000>=me: return 'Bergerak'
  return 'Tertinggal'
d['kuadran']=d.apply(q,axis=1)
m={'Papua Barat Daya':'Papua Barat','Papua Selatan':'Papua','Papua Tengah':'Papua','Papua Pegunungan':'Papua'}
e2=e.copy();e2['prov34']=e2.provinsi.replace(m)
g=e2.groupby(['tahun_data','prov34']).jumlah_usaha.sum().unstack(0);g['growth']=(g[2024]/g[2020]-1)*100
pp=d.groupby('pulau').agg(usaha=('jumlah_usaha','sum'),pend=('penduduk','sum'))
pp['share_usaha']=pp.usaha/pp.usaha.sum()*100;pp['share_pend']=pp.pend/pp.pend.sum()*100;pp['per1000']=pp.usaha/pp.pend*1000
pp['growth']=(pp.usaha/e2[e2.tahun_data==2020].groupby('pulau').jumlah_usaha.sum()-1)*100
nat=4400972/p[(p.tahun==2024)&(p.provinsi=='Indonesia')].penduduk.iloc[0]*1000
print(len(d),'r',round(r,3),'rho',round(rs,3),'med',mi,round(me,2),'nat',round(nat,2))
print(d.kuadran.value_counts().to_dict())
for k in ['Siap','Potensial','Bergerak','Tertinggal']: print(k, list(d[d.kuadran==k].provinsi))
print(pp.round(2).to_string())
d.round(3).to_csv(f'{D}/analisis_provinsi_2024.csv',index=False)
json.dump({"prov":d[['provinsi','pulau','jumlah_usaha','penduduk','per1000','share','internet_total','internet_kota','internet_desa','kuadran']].round(2).replace({np.nan:None}).to_dict('records'),
 "r":round(r,2),"rho":round(rs,2),"medInternet":mi,"medPer1000":round(me,2),"nat1000":round(nat,2),
 "pulau":pp.reset_index().round(2).to_dict('records'),"growthProv":g['growth'].round(1).dropna().to_dict()},open(f'{D}/derived.json','w'),ensure_ascii=False)
