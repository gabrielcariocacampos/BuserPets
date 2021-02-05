<template>
    <v-layout justify-center align-center>
        <form>
      <v-text-field
        label="Nome"
      ></v-text-field>
      <v-text-field
        label="Cidade"
      ></v-text-field>
      <v-text-field
        label="Endereço"
      ></v-text-field>
      <v-text-field
        label="Casa ou AP"
      ></v-text-field>
      <v-text-field
         label="Disponibilidade de Horas"
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

