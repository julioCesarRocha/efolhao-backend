"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[503],{2503:function(e,t,s){s.r(t),s.d(t,{default:function(){return S}});var a=s(998),o=s(3059),i=s(3687),r=function(){var e=this,t=e._self._c;return t(a.Z,[t(i.Z),t("Usuario"),t(o.Z)],1)},n=[],l=s(3694),c=s(903),u=s(4886),d=s(266),m=s(9256),p=s(5125),h=s(1713),v=s(8704),f=function(){var e=this,t=e._self._c;return t(a.Z,[t(p.Z,[t(m.Z,{attrs:{fluid:""}},[t("div",[t(l.Z,{attrs:{value:e.showSuccessAlert,type:"success",dismissible:""},on:{input:function(t){e.showSuccessAlert=!1}}},[e._v(" Cadastro do paciente relizado com sucesso! ")]),t(u.EB,{staticClass:"title"},[t("h3",[e._v("Cadastrar Paciente")])])],1),t(h.Z,[t(d.Z,{attrs:{cols:"12",md:"4"}},[t(v.Z,{attrs:{label:"Nome",required:""},model:{value:e.nome,callback:function(t){e.nome=t},expression:"nome"}})],1),t(d.Z,{attrs:{cols:"12",md:"4"}},[t(v.Z,{attrs:{label:"CPF"},model:{value:e.cpf,callback:function(t){e.cpf=t},expression:"cpf"}})],1),t(d.Z,{attrs:{cols:"12",md:"4"}},[t(v.Z,{attrs:{label:"Data Nascimento",type:"date",rules:e.dateRules,clearable:""},model:{value:e.data_nascimento,callback:function(t){e.data_nascimento=t},expression:"data_nascimento"}})],1)],1),t(h.Z,[t(d.Z,{attrs:{cols:"12",md:"2"}},[t(v.Z,{attrs:{label:"Peso",required:""},model:{value:e.peso,callback:function(t){e.peso=t},expression:"peso"}})],1),t(d.Z,{attrs:{cols:"12",md:"2"}},[t(v.Z,{attrs:{label:"Reg",required:""},model:{value:e.reg,callback:function(t){e.reg=t},expression:"reg"}})],1),t(d.Z,{attrs:{cols:"12",md:"2"}},[t(v.Z,{attrs:{label:"Convênio",required:""},model:{value:e.convenio,callback:function(t){e.convenio=t},expression:"convenio"}})],1),t(d.Z,{attrs:{cols:"12",md:"2"}},[t(v.Z,{attrs:{label:"Leito",required:""},model:{value:e.leito,callback:function(t){e.leito=t},expression:"leito"}})],1)],1)],1),t("div",{attrs:{id:"div-botoes",align:"right"}},[t(c.Z,{staticClass:"mr-4",attrs:{color:"success"},on:{click:e.salvar}},[e._v("Salvar")]),t(c.Z,{staticClass:"mr-4",attrs:{color:"error"}},[e._v(" Cancelar ")])],1)],1)],1)},Z=[],b=(s(7658),s(3988)),g={name:"UsuarioComponent",data(){return{showSuccessAlert:!1,nome:this.nome,cpf:this.cpf,data_nascimento:this.data_nascimento,peso:this.peso,reg:this.reg,convenio:this.convenio,leito:this.leito,selectedDate:null,dateRules:[e=>!!e||"A data é obrigatória",e=>/^\d{4}-\d{2}-\d{2}$/.test(e)||"A data deve estar no formato YYYY-MM-DD"]}},methods:{mounted(){},async salvar(){const e={nome:this.nome,cpf:this.cpf,data_nascimento:this.data_nascimento,peso:this.peso,reg:this.reg,convenio:this.convenio,leito:this.leito},t=await b.Z.criarUsuario(e),s=t.data.id;201===t.status&&(this.showSuccessAlert=!0,1==this.showSuccessAlert&&setTimeout((()=>{this.$router.push({name:"Pacientes",params:{id:s}})}),3e3))}}},_=g,k=s(1001),C=(0,k.Z)(_,f,Z,!1,null,"c5e7c6ae",null),x=C.exports,U={components:{Usuario:x}},w=U,A=(0,k.Z)(w,r,n,!1,null,null,null),S=A.exports},3988:function(e,t,s){var a=s(9669),o=s.n(a);const i="http://127.0.0.1:8000/",r=o().create({baseURL:i});t["Z"]={getPacientes:()=>r.get("usuario"),getUsuario:e=>r.get(`usuario/${e}`),criarUsuario:e=>r.post("usuario/",e),atualizarUsuario:(e,t)=>r.put(`usuario/${e}`,t),deletarUsuario:e=>r.delete(`usuario/${e}`)}}}]);
//# sourceMappingURL=503.58dc2f3d.js.map