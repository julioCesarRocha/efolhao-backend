"use strict";(self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[]).push([[141],{141:function(t,e,a){a.r(e),a.d(e,{default:function(){return w}});var n=a(998),s=a(3059),r=function(){var t=this,e=t._self._c;return e(n.Z,[e("Pacientes"),e(s.Z)],1)},o=[],i=a(903),u=a(4886),c=a(9223),l=a(5808),d=a(4525),h=a(7988),p=function(){var t=this,e=t._self._c;return e(n.Z,[e(u.EB,[e("h2",[t._v("Pacientes")]),e(i.Z,{staticClass:"ml-auto mr-2",attrs:{color:"success"},on:{click:t.cadastrarPaciente}},[t._v("Novo")])],1),e(u.ZB,[e(l.Z,t._l(t.patients,(function(a){return e(d.Z,{key:a.id,on:{click:function(e){return t.detalharPaciente(a.id,a.nome,a.data_criacao)}}},[e("input",{attrs:{type:"hidden"},domProps:{value:a.id}}),e(h.km,[e(h.V9,[t._v(t._s(a.nome))]),e(h.oZ,[t._v(t._s(new Date(a.data_nascimento).toLocaleDateString("pt-BR"))+" ")]),e(c.Z,{attrs:{thickness:7}})],1)],1)})),1)],1)],1)},m=[],f=(a(7658),a(3988)),v={data(){return{headers:[{text:"Nome",value:"nome"},{text:"Idade",value:"idade"}],patients:[]}},mounted(){this.fetchPatients()},methods:{async fetchPatients(){try{const t=await f.Z.getPacientes();this.patients=t.data}catch(t){console.error(t)}},detalharPaciente(t,e,a){console.log(this.patients),this.$router.push({name:"MenuComponent",params:{id:t,nome:e,dataInternacao:a}})},cadastrarPaciente(){this.$router.push({name:"UsuarioComponent"})}}},Z=v,_=a(1001),P=(0,_.Z)(Z,p,m,!1,null,"2483f5db",null),k=P.exports,g={components:{Pacientes:k}},U=g,b=(0,_.Z)(U,r,o,!1,null,null,null),w=b.exports},3988:function(t,e,a){var n=a(9669),s=a.n(n);const r="e-viss.azurewebsites.net/",o=s().create({baseURL:r});e["Z"]={getPacientes:()=>o.get("usuario"),getUsuario:t=>o.get(`usuario/${t}`),criarUsuario:t=>o.post("usuario/",t),atualizarUsuario:(t,e)=>o.put(`usuario/${t}`,e),deletarUsuario:t=>o.delete(`usuario/${t}`)}}}]);
//# sourceMappingURL=141.2617af11.js.map