import {
  ActionIcon,
  Container,
  Flex,
  Input,
  ScrollArea,
  Group,
  Loader,
} from "@mantine/core";
import { useConversation } from "@/app/customHooks/conversationHooks";
import {
  getFullConversation,
  Prompt,
  QueryRole,
} from "@/restHelpers/conversationHelper";
import { useEffect, useRef, useState } from "react";
import { IoSend } from "react-icons/io5";
import MessageBox from "../Messages/MessageBox";
import { postQuery } from "@/restHelpers/conversationHelper";
const MainChat = () => {
  const { conversationId, setConversationId } = useConversation();
  const [currPrompt, setCurrPrompt] = useState<string>("");
  const [messages, setMessages] = useState<Prompt[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const bottomLine = useRef<HTMLDivElement>();

  useEffect(() => {
    const getChatHistory = async () => {
      const { messages } = await getFullConversation(conversationId);
      setMessages(messages);
    };
    getChatHistory();
  }, [conversationId, loading]);

  useEffect(() => {
    bottomLine.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendPrompt = async () => {
    const sentPrompt: Prompt = {
      role: QueryRole.USER,
      content: currPrompt,
    };
    setMessages((prevMessages: Prompt[]) => [...prevMessages, sentPrompt]);
    setCurrPrompt("");
    try {
      setLoading(true);
      const { id } = await postQuery(conversationId, sentPrompt);
      setConversationId(id);
      setLoading(false);
    } catch (e) {
      alert(e);
    }
  };
  return (
    <Container>
      <ScrollArea h={850}>
        {messages !== undefined && messages.length > 0 ? (
          <>
            {messages.map((item, index) => (
              <MessageBox role={item.role} content={item.content} key={index} />
            ))}
          </>
        ) : (
          <></>
        )}
        <div ref={bottomLine} />
      </ScrollArea>
      <Container hidden={conversationId === undefined}>
        <Input
          disabled={loading}
          value={currPrompt}
          onChange={(event) => setCurrPrompt(event.target.value)}
          placeholder="Chat here..."
          size="lg"
          rightSectionPointerEvents="all"
          rightSection={
            <ActionIcon size={"lg"} onClick={async () => sendPrompt()}>
              {loading ? <Loader color="white" size={"sm"} /> : <IoSend />}
            </ActionIcon>
          }
        />
      </Container>
    </Container>
  );
};

export default MainChat;
