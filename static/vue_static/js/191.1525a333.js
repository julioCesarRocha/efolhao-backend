"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[191],{9191:function(s,e,t){t.r(e),t.d(e,{default:function(){return P}});var a=t(998),o=t(3059),l=function(){var s=this,e=s._self._c;return e(a.Z,[e("Neurologico"),e(o.Z)],1)},i=[],r=t(3694),c=t(903),u=t(4886),n=t(266),d=t(9256),p=t(5125),g=t(1713),h=t(2328),m=t(8704),Z=function(){var s=this,e=s._self._c;return e(a.Z,[e(p.Z,[e(d.Z,{attrs:{fluid:""}},[e("div",[e(r.Z,{attrs:{value:s.showSuccessAlert,type:"success",dismissible:""},on:{input:function(e){s.showSuccessAlert=!1}}},[s._v(" Cadastro relizado com sucesso! ")]),e(u.EB,{staticClass:"title"},[e("h3",[s._v("Dados Neurológicos")])])],1),e(g.Z,[e(n.Z,{attrs:{cols:"12",md:"6"}},[e(m.Z,{attrs:{label:"Glasgow",required:""},model:{value:s.glasgow,callback:function(e){s.glasgow=e},expression:"glasgow"}})],1),e(n.Z,{attrs:{cols:"12",md:"6"}},[e(h.Z,{attrs:{label:"Pupilas",items:s.listaPupilas,required:""},model:{value:s.pupilas,callback:function(e){s.pupilas=e},expression:"pupilas"}})],1)],1),e(g.Z,[e(n.Z,{attrs:{cols:"12",md:"6"}},[e(m.Z,{attrs:{label:"SAS",required:""},model:{value:s.sas,callback:function(e){s.sas=e},expression:"sas"}})],1),e(n.Z,{attrs:{cols:"12",md:"6"}},[e(m.Z,{attrs:{label:"Dor",required:""},model:{value:s.dor,callback:function(e){s.dor=e},expression:"dor"}})],1)],1),e(g.Z,[e(n.Z,{attrs:{cols:"12",md:"6"}},[e(m.Z,{attrs:{label:"PIC",required:""},model:{value:s.pic,callback:function(e){s.pic=e},expression:"pic"}})],1),e(n.Z,{attrs:{cols:"12",md:"6"}},[e(m.Z,{attrs:{label:"SjO2",required:""},model:{value:s.sj02,callback:function(e){s.sj02=e},expression:"sj02"}})],1)],1)],1),e("div",{attrs:{id:"div-botoes",align:"right"}},[e(c.Z,{staticClass:"mr-4",attrs:{color:"success"},on:{click:s.salvar}},[s._v("Salvar")]),e(c.Z,{staticClass:"mr-4",attrs:{color:"error"}},[s._v(" Cancelar ")])],1)],1)],1)},v=[],f=(t(7658),t(9669)),b=t.n(f);const w="e-viss.azurewebsites.net/",k=b().create({baseURL:w});var S={getNeurologico:()=>k.get("neurologico"),getDadosNeurologicos:s=>k.get(`neurologico/${s}`),inserirDadosNeurologicos:s=>k.post("neurologico/",s)},C={name:"NeurologicoComponent",data(){return{showSuccessAlert:!1,glasgow:this.glasgow,pupilas:this.pupilas,sas:this.sas,dor:this.dor,pic:this.pic,sj02:this.sj02,listaPupilas:["D=E","D>E","D<E","Sem Reação"]}},methods:{mounted(){},async salvar(){const s={glasgow:this.glasgow,pupilas:this.pupilas,sas:this.sas,dor:this.dor,pic:this.pic,sj02:this.sj02,id_usuario:this.$route.params.id},e=await S.inserirDadosNeurologicos(s);201===e.status&&(this.showSuccessAlert=!0,1==this.showSuccessAlert&&setTimeout((()=>{this.$router.push({name:"Pacientes",params:{id:this.$route.params.id}})}),3e3))}}},_=C,j=t(1001),x=(0,j.Z)(_,Z,v,!1,null,"d453d54e",null),D=x.exports,N={components:{Neurologico:D}},q=N,A=(0,j.Z)(q,l,i,!1,null,null,null),P=A.exports}}]);
//# sourceMappingURL=191.1525a333.js.map