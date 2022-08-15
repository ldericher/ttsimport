<template>
  <v-select
    label="Deck Language"
    prepend-icon="mdi-translate"
    v-model="language"
    @input="change"
    :items="languages"
    dense
    filled
  />
</template>

<script>
export default {
  name: "LanguageSelect",

  data: () => ({
    language: "",
  }),

  mounted() {
    this.change();
  },

  computed: {
    languages: () => [
      { value: "en", text: "English" },
      { value: "fr", text: "French" },
      { value: "de", text: "German" },
      { value: "it", text: "Italian" },
      { value: "ja", text: "Japanese (tooltips only)" },
      { value: "es", text: "Spanish" },
    ],

    language_values() {
      var res = [];

      for (const lang of this.languages) {
        res.push(lang.value);
      }

      return res;
    },

    current_language() {
      if (this.language_values.includes(this.language)) {
        return this.language;
      } else {
        return "en";
      }
    },
  },

  methods: {
    change() {
      this.$root.ttsimport_language = this.current_language;
    },
  },
};
</script>
