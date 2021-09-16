<template>
  <v-list flat>
    <template v-for="(deck, idx) in decks">
      <v-list-item :key="idx">
        <v-list-item-avatar>
          <v-icon color="primary">mdi-cards</v-icon>
        </v-list-item-avatar>

        <v-list-item-content class="noselect">
          {{ deck.name }} ({{ deck.card_count }} Cards)
        </v-list-item-content>

        <v-tooltip left>
          <template v-slot:activator="{ on, attrs }">
            <v-list-item-action
              v-if="deck.card_count != 50"
              v-bind="attrs"
              v-on="on"
            >
              <v-icon color="warning">mdi-flash-alert</v-icon>
            </v-list-item-action>
          </template>
          <span>Non-Standard deck size!</span>
        </v-tooltip>

        <v-list-item-action>
          <v-btn @click="delete_deck(idx)" color="error" icon outlined>
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>

      <v-divider
        v-if="idx != decks.length - 1"
        :key="idx + '_div'"
        class="my-2"
        role="presentation"
      />
    </template>

    <v-progress-linear v-if="loading" indeterminate />

    <v-form ref="form" @submit.prevent="add_deck" v-model="valid">
      <v-list-item>
        <v-list-item-content>
          <v-text-field
            placeholder="Paste FF Decks Link or ID here"
            hint="e.g. https://ffdecks.com/deck/6272690272862208 or 6272690272862208"
            v-model="new_deck_id"
            :rules="new_deck_id_rules"
            dense
            filled
          >
            <template v-slot:append-outer>
              <v-btn
                color="primary"
                type="submit"
                :disabled="!valid"
                icon
                outlined
              >
                <v-icon>mdi-check</v-icon>
              </v-btn>
            </template>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
    </v-form>
  </v-list>
</template>

<script>
export default {
  name: "DecksList",

  props: {
    value: Array,
  },

  data: () => ({
    decks: [],
    valid: false,
    loading: false,
    new_deck_id: "",
    new_deck_id_rules: [
      (v) =>
        !v ||
        /^((https?:\/\/)?ffdecks\.com(\/+api)?\/+deck\/+)?([0-9]+)/.test(v) ||
        "Deck ID is malformed",
    ],
  }),

  mounted() {
    if (Array.isArray(this.value)) {
      for (const deck_id of this.value) {
        this.decks.push({ id: String(deck_id) });
      }
    }

    this.$emit("input", this.current_deck_ids);
  },

  computed: {
    current_deck_ids() {
      var res = [];

      for (const deck of this.decks) {
        res.push(deck.id);
      }

      return res;
    },
  },

  methods: {
    add_deck() {
      if (this.new_deck_id && this.valid) {
        const new_deck_id = this.new_deck_id;
        this.$refs.form.reset();

        // start loading
        this.loading = true;

        this.$http({
          url: this.ttsimport_api_baseurl + "/ffdecks/summaries",
          method: "POST",
          data: { deck_ids: [new_deck_id] },
        })
          .then((response) => {
            if (response.data.length > 0) {
              const data = response.data[0];

              if (!this.current_deck_ids.includes(data.deck_id)) {
                this.decks.push({
                  id: data.deck_id,
                  name: data.name,
                  card_count: data.card_count,
                });
                this.$emit("input", this.current_deck_ids);
              }
            }
            this.loading = false;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },

    delete_deck(index) {
      if (index < this.decks.length) {
        this.decks.splice(index, 1);

        this.$emit("input", this.current_deck_ids);
      }
    },
  },
};
</script>

<style scoped>
.noselect {
  user-select: none;
}
</style>
