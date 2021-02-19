<template>
 <v-layout align-center justify-center>
    <template>
      <div class="modelo">
        <v-flex v-for="(item, index) in items" :key="index"> 
          <v-card class="mx-auto" max-width="344px">
              <v-img :src="item.image" width="100%" height="auto"></v-img>
              <v-card-title class="ad"> {{item.nomepessoal}}</v-card-title>  
                <ul>
                  <li><label for="texto">Nome:</label><v-text class="bd">{{item.nomeanimal}}</v-text></li>
                  <li><label for="texto">Idade:</label><v-text class="bd">{{item.idade}}</v-text></li>
                  <li><label for="texto">Raça:</label><v-text class="bd">{{item.raça}}</v-text></li>
                  <li><label for="texto">Costumes:</label><v-text class="bd">{{item.costumes}}</v-text></li>
                  <li><label for="texto">Alimentação:</label><v-text class="bd">{{item.alimentação}}</v-text></li>
                  <li><label for="texto">Gosta de crianças ?</label><v-text class="bd">{{item.gosta}}</v-text></li>
                </ul>
              <v-divider :key="index"></v-divider>
              <v-btn class="adotar" @click="Adotar(item)"
                ><v-icon dark left>email</v-icon> Adotar </v-btn>
          </v-card>
        </v-flex>
       </div>
    </template>
  </v-layout>
</template>

<script>

import AppApi from '~apijs'
import Pais from '~/components/Pais.vue'

export default {
  data () {
    return {
      items:[],
      resultado: '',
      text: '',
      nomepessoal: '',
      nomeanimal: '',
      idade: '',
      raça: '',
      costumes: '',
      alimentação: '',
      gosta: ''
    }
  },
  created () {
    AppApi.listaranimais().then(response => {this.items = response.data})
  },
  components: {
    Pais,
  },
  methods: {
    Adotar(item){
      this.text += `Olá! Desejamos que ambos desfrutem de uma agradável aventura... Voltem Sempre! \n`;
      this.text += `Nome da pessoa: ${item.nomepessoal}\n`;
      this.text += `Nome do animal: ${item.nomeanimal}\n`;
      this.text += `Idade: ${item.idade}\n`;
      this.text += `Raça: ${item.raça}\n`;
      this.text += `Costume(s): ${item.costumes}\n`;
      this.text += `Alimentação: ${item.alimentação} \n`;
      this.text += `Gosta de crianças: ${item.gosta} \n`;
      this.text += `Olá ${item.nomepessoal}, você confirma as informações acima sobre o seu PET ?! Quando posso busca-lo ?! `
      this.apilink = "http://api";
      this.apilink +=
        ".whatsapp.com/send?phone=+55" +
        item.telefone +
        "&text=" +
        encodeURI(this.text);
      window.open(this.apilink);
      }
     },
  }

</script>

<style>
  .ad {
    font-size: 32px;
    color: black;
    margin: 8px;
    font: serif;
  }
  .bd {
    font-size: 20px;
    color: black;
    margin: 4px;
    font: serif;
  }
  .mx-auto {
    display: flex;
    flex-flow: column wrap;
    padding: 1.5rem;
    box-shadow: 0px 2px 22px #26395338;
  }
  .modelo {
    display: flex;
    flex-flow: row wrap;
    flex-grow: 1;
  }
</style>


