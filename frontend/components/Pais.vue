<template>
    <v-layout justify-center align-center>
        <h1> Lista de Pais </h1>
    </v-layout>
</template>

<script>
import Pais from '~/components/Pais.vue'
import Api from '~apijs'

export default {
    data () {
        return {
          pais: []
        }
    },
    created() {
        AppApi.list_pais().then(response => {
            this.pais = response.data
            console.log('pais')
            console.log(this.pais)
        })
        
    }
    
}
</script>