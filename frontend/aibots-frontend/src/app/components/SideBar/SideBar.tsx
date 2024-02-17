import { getAllConversations } from "@/restHelpers/conversationHelper";
import { ActionIcon, AppShell, Button, Divider, Skeleton } from "@mantine/core";
import { IoAdd } from "react-icons/io5";
import { useEffect } from "react";
import { useQuery } from "react-query";
import { useConversation } from "@/app/customHooks/conversationHooks";

const SideBar = () => {
  const { conversationId, setConversationId } = useConversation();
  const { isLoading, error, data } = useQuery({
    queryKey: ["convoAll"],
    queryFn: getAllConversations,
  });
  const setConv = (convoId: string) => {
    setConversationId(convoId);
  };
  return (
    <AppShell.Navbar p="md">
      <Button leftSection={<IoAdd />}>Add Conversation</Button>
      <Divider mt={8} />
      <p className="text-gray-300">Conversations 💬</p>
      {data?.data.map((item, index) => {
        return (
          <Button
            fullWidth
            mt={8}
            variant="light"
            key={item._id}
            onClick={() => setConv(item._id)}
          >
            {item.name}
          </Button>
        );
      })}
    </AppShell.Navbar>
  );
};

export default SideBar;
