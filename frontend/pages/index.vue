<template>
  <v-layout class="foto" align-center justify-center>
    <label class="texto"> Adoção é também doação: de carinho, respeito e atenção, experimentar a forma mais pura de amor e gratidão, 
      não importa a raça, pois todos os an  imais tem a sua graça!!! 
       A ideia aqui é simples, você precisa viajar por alguns dias ou semanas e não sabe com quem deixar seu melhor amigo, seja ele:
       um cachorro, gato ou passarinho ?? 
       Nós iremos solucionar o seu problema trazendo interação entre os amigos e melhores amigos, desta Empresa incrível, que é exemplo de empatia 
       e companheirismo entre seus colaboradores.
       Agora é só se programar para viajar e cadastrar seu PET com algum tempo de antecedência... Encontre novos amigos que sejam a sua cara e Divirta-se!</label>
    <div>
     <v-btn x-larger color="black" dark><router-link :to="{name: 'cadastreseuanimal'}">Cadastre seu animalzinho!</router-link></v-btn>
     <v-btn x-larger color="black" dark ><router-link :to="{name: 'animaisparacuidar'}">Animais para cuidar!</router-link></v-btn>
   </div>
   <div class="fotos">
    <v-img src="https://super.abril.com.br/wp-content/uploads/2017/10/gatos.png"></v-img>
    <v-img src="http://www.sjc.sp.gov.br/media/21585/img_5158.jpg?anchor=center&mode=crop&width=940&height=626&rnd=131730368860000000"></v-img>
    <v-img src="https://s2.glbimg.com/Mu_uGOOzZYoYMI5BtTQ71M5aOuE=/0x174:720x847/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2017/o/p/xl4vYoTIGf6EewDXxRaw/22407481-1520241258061995-397242158-n.jpg"></v-img>   
   </div>
  </v-layout>
</template>

<script>

export default {
  data () {
    return {}
  }
}
</script>

<style>
.texto {
  font-family: sans-serif;
  font-size: 22px;
  font: serif;
  margin:15px;
 
}
.fotos {
  display: flex;
  justify-content: space-around;
  width: 1300px;
  height: 400px;
  margin: 25px;
}
.foto {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

</style>
