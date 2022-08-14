<template>
  <v-btn
    @click="$emit('click')"
    :icon="sm_and_down"
    :tabindex="tabindex"
    :href="href"
    :target="href ? '_blank' : ''"
    text
  >
    <v-icon :left="!sm_and_down">{{ icon }}</v-icon>
    <span class="hidden-sm-and-down ml-2">{{ text }}</span>
  </v-btn>
</template>

<script>
export default {
  name: "IconTextButton",

  props: {
    icon: {
      type: String,
      required: true,
    },

    text: {
      type: String,
      required: true,
    },

    href: String,

    tabindex: {
      type: Number,
      default: -1,
    },
  },

  computed: {
    sm_and_down() {
      return this.$vuetify.breakpoint.smAndDown;
    },
  },
};
</script>