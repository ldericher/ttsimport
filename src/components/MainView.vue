<template>
  <v-main>
    <v-container>
      <v-img
        :src="require('../assets/yavook_big.png')"
        class="my-3 mx-auto"
        contain
        height="200"
      />

      <decks />
    </v-container>
  </v-main>
</template>

<script>
import Decks from "./Decks.vue";

export default {
  name: "MainView",

  components: {
    Decks,
  },
};
</script>
