<template>
  <v-list-item>
    <v-list-item-avatar>
      <v-icon :color="failed ? 'error' : 'primary'">mdi-cards</v-icon>
    </v-list-item-avatar>

    <v-list-item-content class="noselect">
      <v-progress-linear v-if="loading" indeterminate />
      <v-alert
        v-else-if="failed"
        type="error"
        class="mb-0"
        :icon="false"
        outlined
        dense
      >
        {{ deck_name }} (Deck ID "{{ deck_id }}")
      </v-alert>
      <template v-else> {{ deck_name }} ({{ card_count }} Cards) </template>
    </v-list-item-content>

    <v-list-item-icon>
      <v-tooltip v-if="successful" left>
        <template v-slot:activator="{ on }">
          <v-btn
            v-if="card_count !== 50"
            v-on="on"
            color="warning"
            class="ml-2"
            icon
            outlined
          >
            <v-icon>mdi-flash-alert</v-icon>
          </v-btn>
        </template>
        Non-Standard deck size!
      </v-tooltip>

      <v-btn @click="delete_self" color="error" class="ml-2" icon outlined>
        <v-icon>mdi-delete</v-icon>
      </v-btn>

      <v-btn
        v-if="successful"
        @click="download"
        color="success"
        class="ml-2"
        icon
        outlined
      >
        <v-icon>mdi-download</v-icon>
      </v-btn>
    </v-list-item-icon>
  </v-list-item>
</template>

<script>
export default {
  name: "Deck",

  props: {
    deck_id: String,
  },

  data: () => ({
    deck_name: null,
    card_count: null,
  }),

  computed: {
    loading() {
      return this.deck_name === null;
    },

    successful() {
      return !this.loading && this.card_count !== null;
    },

    failed() {
      return !(this.loading || this.successful);
    },
  },

  watch: {
    deck_id: {
      immediate: true,
      handler: "update_deck_id",
    },
  },

  methods: {
    download() {
      this.$http({
        url: this.ttsimport_api_baseurl + "/ffdecks/deck",
        method: "POST",
        responseType: "blob",
        data: {
          language: this.$root.ttsimport_language,
          deck_id: this.deck_id,
        },
      })
        .then((response) => {
          // save response
          let blob = new Blob([response.data], { type: "application/json" });

          // redirect to browser
          let link = document.createElement("a");
          link.href = window.URL.createObjectURL(blob);

          // find suggested file name
          let cd_header = response.request.getResponseHeader(
            "Content-Disposition"
          );
          let fn_start_marker = "filename=";
          let suggested_fn_pos =
            cd_header.indexOf(fn_start_marker) + fn_start_marker.length;
          link.download = cd_header.substr(suggested_fn_pos);

          // actually download
          link.click();
        })
        .catch((error) => {
          console.error(error);
          this.deck_name = "Failed to load JSON for deck, try again";
          this.card_count = null;
        });
    },

    update_deck_id(new_deck_id) {
      this.deck_name = null;

      this.$http({
        method: "POST",
        url: this.ttsimport_api_baseurl + "/ffdecks/summary",
        data: {
          language: this.$root.ttsimport_language,
          deck_id: new_deck_id,
        },
      })
        .then((response) => {
          this.deck_name = response.data.name;
          this.card_count = response.data.card_count;
        })
        .catch((error) => {
          console.error(error);
          this.deck_name = "Failed to load deck";
          this.card_count = null;
        });
    },

    delete_self() {
      this.$emit("delete");
    },
  },
};
</script>

<style scoped>
.noselect {
  user-select: none;
}
</style>