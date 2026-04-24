<script setup lang="ts">
import { useColorMode } from "@vueuse/core";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Moon, Sun } from "lucide-vue-next";

// Pass { disableTransition: false } to enable transitions
const mode = useColorMode({ disableTransition: false });
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button variant="outline">
        <Sun v-if="mode === 'light'" class="h-5 w-5" />
        <Moon v-else class="h-5 w-5" />

        <span class="sr-only">Toggle theme</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent>
      <DropdownMenuItem @click="mode = 'light'"> Light </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'dark'"> Dark </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'auto'"> System </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
