<template>
  <footer
    v-if="$nav.currentLayout !== 'cover'"
    class="absolute bottom-0 left-3 p-4"
  >
    {{ $nav.currentPage }}
  </footer>
</template>
