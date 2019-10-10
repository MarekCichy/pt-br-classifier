<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex>
        <!-- IMPORTANT PART! -->
    <span class="font-weight-bold" style="font-size:20pt">classificador de sotaques</span>
    <v-img
      src="http://marekcichy.alwaysdata.net/portvsbr.jpg"
      lazy-src="http://marekcichy.alwaysdata.net/portvsbr.jpg"
      aspect-ratio="1"
      class="grey lighten-2"
      max-width="1200"
      max-height="300"
    ></v-img><span class="font-weight-light" style="font-size:10pt">Fotos de <a href="https://www.pexels.com/photo/road-with-crowd-2014700/">Gabriel Santos</a> e <a href="https://www.pexels.com/photo/people-at-city-1534560/">Lisa Fotios</a></span><br><br>
	<span class="font-weight-light">O classificador de sotaques reconhece textos segundo sua variedade do português (europeu vs. brasileiro). <br>Envie-nos um texto e abaixo vai receber a classificação (PT ou BR) e o nível de confiança do modelo. <br> O modelo <b><a href="https://youtu.be/t11JYaJcpxg?t=79" target="_blank">errou</a></b>? Informe a gente em classificadorptbr(at)gmail.com. <br> Leia mais sobre o projeto <a href="https://github.com/MarekCichy/pt-br-classifier/blob/master/README.md">aqui</a>.</span>
	<br><br>
		<v-divider></v-divider>
		<v-form
		@submit="submit"
        onSubmit="return false;">
          <v-text-field
            v-model="ptText"
            label="Texto para classificar"
            required
          ></v-text-field>
<v-btn @click="submit">enviar</v-btn>
          <v-btn @click="clear">limpar</v-btn>
        </v-form>
<br/>
      
<h1 v-if="predictedClass">O texto foi classificado como: {{ predictedClass }} com {{predictedConfidence}} de confiança.</h1>
<!-- END: IMPORTANT PART! -->
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
  import axios from 'axios'
export default {
    name: 'HelloWorld',
    data: () => ({
      ptText: '',
      predictedClass : ''
    }),
    methods: {
    submit () {
	this.predictedClass = ''
	axios.get('https://mariankowlak.eu.pythonanywhere.com/predict?text='+this.ptText)
	.then((response) => {
		this.predictedClass = response.data.sotaque
		this.predictedConfidence = response.data.confidence
      })
    },
    clear () {
		this.ptText = ''
		this.predictedClass = ''
    }
  }
}
</script>