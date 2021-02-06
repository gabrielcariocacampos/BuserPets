<template>
    <v-layout justify-center align-center>
        <form>
      <v-text-field
        label="Nome" v-model="nomeanimal"
      ></v-text-field>
      <v-text-field
        label="Raça/Espécie" v-model="raça"
      ></v-text-field>
      <v-text-field
        label="Costumes" v-model="costumes"
      ></v-text-field>
      <v-text-field
        label="Alimentação" v-model="alimentação"
      ></v-text-field>
      <v-text-field
        label="Gosta de crianças ?" v-model="gosta"
      ></v-text-field>
      <v-text-field
        label="Idade" v-model="idade"
        type="number"
      ></v-text-field>
      
        <v-btn class="conclude-order" color="success" @click="cadastroanimal()"
          ><v-icon dark left>local_shipping</v-icon> Finalizar</v-btn>
        <small v-if = "acerto">Cadastro Concluído</small>
    </form>
    </v-layout>
</template>

<script>

import AppApi from '~apijs'

export default {
    data () {
        return { nomeanimal: '',
        raça: '',
        costumes: '',
        alimentação: '',
        gosta: '',
        idade: '',
        resultado: '',
        acerto: false
        }
    },
    methods: {
      cadastroanimal () {
        const status=AppApi.cadastroanimal (this.nomeanimal, this.raça, this.costumes, this.alimentação, this.gosta, this.idade)
        if (status){
          this.acerto = true
        }
        else{this.acerto = false
        } 
      }
    }
}
</script>

