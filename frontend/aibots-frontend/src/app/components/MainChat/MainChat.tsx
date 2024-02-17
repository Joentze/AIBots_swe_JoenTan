import {
  ActionIcon,
  Container,
  Flex,
  Input,
  ScrollArea,
  Group,
} from "@mantine/core";
import { useConversation } from "@/app/customHooks/conversationHooks";
import { getFullConversation, Prompt } from "@/restHelpers/conversationHelper";
import { useEffect, useState } from "react";
import { IoSend } from "react-icons/io5";

const MainChat = () => {
  const { conversationId, setConversationId } = useConversation();
  const [currPrompt, setCurrPrompt] = useState<string>("");
  const [messages, setMessages] = useState<Prompt[]>();
  useEffect(() => {
    const getChatHistory = async () => {
      const { messages } = await getFullConversation(conversationId);
      setMessages(messages);
    };
    getChatHistory();
  }, [conversationId]);
  return (
    <Container>
      <ScrollArea h={850}></ScrollArea>
      <Container>
        <Input
          value={currPrompt}
          onChange={(event) => setCurrPrompt(event.target.value)}
          placeholder="Chat here..."
          size="lg"
          rightSectionPointerEvents="all"
          rightSection={
            <ActionIcon size={"lg"} onClick={() => setCurrPrompt("")}>
              <IoSend />
            </ActionIcon>
          }
        />
      </Container>
    </Container>
  );
};

export default MainChat;
