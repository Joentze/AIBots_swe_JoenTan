"use client";
import Image from "next/image";
import { QueryClient, QueryClientProvider } from "react-query";
import {
  AppShell,
  Burger,
  Group,
  MantineProvider,
  Skeleton,
  useMantineTheme,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import SideBar from "./components/SideBar/SideBar";

const queryClient = new QueryClient();

export default function Home() {
  const [opened, { toggle }] = useDisclosure();

  return (
    <main>
      <QueryClientProvider client={queryClient}>
        <AppShell
          header={{ height: 60 }}
          navbar={{
            width: 300,
            breakpoint: "sm",
            collapsed: { mobile: !opened },
          }}
          padding="md"
        >
          <AppShell.Header>
            <Group h="100%" px="md">
              Chat Bot
            </Group>
          </AppShell.Header>
          <AppShell.Navbar p="md">
            <strong>Conversations 💬</strong>
            {Array(15)
              .fill(0)
              .map((_, index) => (
                <Skeleton key={index} h={28} mt="sm" animate={false} />
              ))}
          </AppShell.Navbar>
          <AppShell.Main></AppShell.Main>
        </AppShell>
      </QueryClientProvider>
    </main>
  );
}
