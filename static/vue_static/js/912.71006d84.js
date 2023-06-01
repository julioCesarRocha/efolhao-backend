"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[912],{2912:function(a,s,t){t.r(s),t.d(s,{default:function(){return L}});var e=t(998),o=t(3059),i=t(3687),r=function(){var a=this,s=a._self._c;return s(e.Z,[s(i.Z),s("HemodinamicaApp"),s(o.Z)],1)},c=[],l=t(3694),n=t(903),d=t(4886),p=t(266),u=t(9256),m=t(5125),v=t(1713),h=t(7414),_=t(2540),b=t(8704),Z=function(){var a=this,s=a._self._c;return s(e.Z,[s(m.Z,{attrs:{id:"form-hemodinamica"}},[s(u.Z,{attrs:{fluid:""}},[s("div",[s(l.Z,{attrs:{value:a.showSuccessAlert,type:"success",dismissible:""},on:{input:function(s){a.showSuccessAlert=!1}}},[a._v(" Dados cadastros com sucesso! ")]),s(d.EB,{staticClass:"title"},[s("h3",[a._v("Dados Hemodinâmicos")])])],1),s(v.Z,[s(p.Z,{attrs:{cols:"12",md:"6"}},[s(b.Z,{attrs:{label:"Pressão Venosa Central (PVC)",required:""},model:{value:a.pressao_venosa_central,callback:function(s){a.pressao_venosa_central=s},expression:"pressao_venosa_central"}})],1),s(p.Z,{attrs:{cols:"12",md:"6"}},[s(b.Z,{attrs:{label:"Pressão da Artéria Pulmonar (PAP)",required:""},model:{value:a.pap,callback:function(s){a.pap=s},expression:"pap"}})],1)],1),s(v.Z,[s(p.Z,{attrs:{cols:"12",md:"6"}},[s(b.Z,{attrs:{label:"Pressão de Oclusão da Artéria Pulmonar (POAP)",required:""},model:{value:a.poap,callback:function(s){a.poap=s},expression:"poap"}})],1),s(p.Z,{attrs:{cols:"12",md:"6"}},[s(b.Z,{attrs:{label:"Saturação Venosa de Oxigênio (SVO2)",required:""},model:{value:a.sv02,callback:function(s){a.sv02=s},expression:"sv02"}})],1)],1),s(v.Z,[s(p.Z,{attrs:{cols:"12",md:"6"}},[s(_.Z,[a._v("Índice Cardíaco (IC - (L/min/m2))")]),s(h.Z,{attrs:{step:"0.5","thumb-label":"",ticks:"",min:"0",max:"20"},model:{value:a.ic,callback:function(s){a.ic=s},expression:"ic"}})],1),s(p.Z,{attrs:{cols:"12",md:"6"}},[s(_.Z,[a._v("Débito Cardíaco (DC - (L/min))")]),s(h.Z,{attrs:{step:"0.5","thumb-label":"",ticks:"",min:"0",max:"30"},model:{value:a.debito_cardiaco,callback:function(s){a.debito_cardiaco=s},expression:"debito_cardiaco"}})],1)],1)],1),s("div",{attrs:{id:"div-botoes",align:"right"}},[s(n.Z,{staticClass:"mr-4",attrs:{color:"success"},on:{click:a.salvar}},[a._v("Salvar")]),s(n.Z,{staticClass:"mr-4",attrs:{color:"error"}},[a._v(" Cancelar ")])],1)],1)],1)},f=[],k=(t(7658),t(9669)),A=t.n(k);const C="e-viss.azurewebsites.net/",x=A().create({baseURL:C});var P={listar:()=>x.get("hemodinamica"),salvar:a=>x.post("hemodinamica/",a)},w={name:"HemodinamicaApp",data(){return{showSuccessAlert:!1,pressao_venosa_central:this.pressao_venosa_central,pap:this.pap,poap:this.poap,ic:this.ic,sv02:this.sv02,debito_cardiaco:this.debito_cardiaco}},methods:{mounted(){P.listar().then((a=>{console.log(a.data),this.hemodinamica=a.data}))},async salvar(){const a={pressao_venosa_central:this.pressao_venosa_central,pap:this.pap,poap:this.poap,ic:this.ic,sv02:this.sv02,debito_cardiaco:this.debito_cardiaco,id_usuario:this.$route.params.id},s=await P.salvar(a);201===s.status&&(this.showSuccessAlert=!0,1==this.showSuccessAlert&&setTimeout((()=>{this.$router.push({name:"Pacientes",params:{id:this.$route.params.id}})}),3e3))}}},S=w,g=t(1001),q=(0,g.Z)(S,Z,f,!1,null,"c5015d34",null),D=q.exports,H={components:{HemodinamicaApp:D}},O=H,V=(0,g.Z)(O,r,c,!1,null,null,null),L=V.exports}}]);
//# sourceMappingURL=912.71006d84.js.map