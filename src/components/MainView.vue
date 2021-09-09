<template>
  <v-main>
    <v-container>
      <v-img
        :src="require('../assets/yavook_big.png')"
        class="my-3 mx-auto"
        contain
        height="200"
      />

      <decks-list />
    </v-container>
  </v-main>
</template>

<script>
import DecksList from "./DecksList.vue";

export default {
  name: "MainView",

  components: {
    DecksList,
  },

  mounted() {
    this.$http
      .get("https://api.coindesk.com/v1/bpi/currentprice.json")
      .then((res) => (this.info = res));
  },

  data: () => ({
    info: "",
  }),
};
</script>
