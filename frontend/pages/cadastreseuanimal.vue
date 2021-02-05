<template>
    <v-layout justify-center align-center>
        <form>
      <v-text-field
        label="Nome"
      ></v-text-field>
      <v-text-field
        label="Raça/Espécie"
      ></v-text-field>
      <v-text-field
        label="Costumes"
      ></v-text-field>
      <v-text-field
        label="Alimentação"
      ></v-text-field>
      <v-text-field
        label="Idade"
        type="number"
      ></v-text-field>
      
        <v-btn class="conclude-order" color="success"
          ><v-icon dark left>local_shipping</v-icon> Finalizar</v-btn>
    </form>
    </v-layout>
</template>

<script>

export default {
    data () {
        return {
        }
    },
}
</script>

