<template>
  <v-container>
    <v-form ref="form" @submit.prevent="add_deck" v-model="valid">
      <v-row>
        <v-col cols="12" class="pb-0">
          <v-text-field
            placeholder="Paste FF Decks Link or ID here"
            hint="e.g. https://ffdecks.com/deck/6272690272862208 or 6272690272862208"
            v-model="deck_id"
            :rules="deck_id_rules"
            clearable
            dense
            filled
          >
          </v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="6" class="pt-0">
          <v-btn color="error" @click="$emit('clear')" :disabled="!valid">
            <v-icon left>mdi-close</v-icon>
            Clear decks list
          </v-btn>
        </v-col>

        <v-col cols="6" class="pt-0" align="right" justify="right">
          <v-btn color="success" type="submit" :disabled="!valid">
            <v-icon left>mdi-check</v-icon>
            Add deck
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: "DeckAddForm",

  data: () => ({
    valid: false,
    deck_id: "",
    deck_id_rules: [
      (v) =>
        !v ||
        /^((https?:\/\/)?ffdecks\.com(\/+api)?\/+deck\/+)?([0-9]+)/.test(v) ||
        "Deck ID is malformed",
    ],
  }),

  methods: {
    add_deck() {
      if (this.deck_id && this.valid) {
        this.$emit("new", this.deck_id);
        this.$refs.form.reset();
      }
    },
  },
};
</script>

<style>
</style>