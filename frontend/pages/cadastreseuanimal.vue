<template>
    <v-layout justify-center align-center>
    <form>
      <v-text-field label="Nome Pessoal" v-model="nomepessoa"> </v-text-field>
      <v-text-field label="Telefone com DDD" v-model="telefone"> </v-text-field>
      <v-text-field label="Nome Animal" v-model="nomeanimal"> </v-text-field>
      <v-text-field label="Raça/Espécie" v-model="raça"> </v-text-field>
      <v-text-field label="Costumes" v-model="costumes"> </v-text-field>
      <v-text-field label="Alimentação" v-model="alimentação"> </v-text-field>
      <v-text-field label="Gosta de crianças ?" v-model="gosta"> </v-text-field>
      <v-text-field label="Idade do Animal" v-model="idade" type="number"> </v-text-field>
      <input
       type="file"
       @change="onFileChange($event)"
/>
        <v-btn class="conclude-order" @click="cadastro()"
          ><v-icon dark left>pets</v-icon> Finalizar</v-btn>
        <small v-if = "acerto">Cadastro Concluído</small>
        <small v-if = "erro">{{ this.mensagem }}</small>
    </form>
    </v-layout>
</template>

<script>

import AppApi from '~apijs'

export default {
    data () {
        return { nomepessoa: '',
        telefone: '',
        nomeanimal: '',
        raça: '',
        costumes: '',
        alimentação: '',
        gosta: '',
        idade: 1,
        resultado: '',
        acerto: false,
        erro: false,
        image: null,
        mensagem: ''
        }
    },
    methods: {
      cadastro () {
        this.erro = false
        if (this.nomepessoa === ''){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Nome da Pessoa'
          return
        }
        if (this.telefone === '' && this.telefone.lenght < 10){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Telefone'
          return
        }
        if (this.nomeanimal === ''){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Nome do Animal'
          return
        }

        if (this.raça === ''){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Raça/espécie'
          return
        }

        if (this.costumes === ''){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Costumes'
          return
        }

        if (this.alimentação === ''){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Alimentação'
          return
        }

        if (this.gosta === ''){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Gosta de crianças?'
          return
        }

        if (this.idade === ''){
          this.erro = true
          this.mensagem = 'Erro, preencha o campo Idade do Animal'
          return
        }
        if (this.image === null){
          this.erro = true
          this.mensagem = 'Erro, faça upload de uma imagem do seu animal'
          return
        }
        const status=AppApi.cadastro (this.nomepessoa, this.telefone, this.nomeanimal, this.raça, this.costumes, this.alimentação, this.gosta, this.idade, this.image)
        this.acerto = true
      },
      onFileChange(event) {
        this.image = event.target.files[0]
      },
    }
}
</script>

<style>

</style>