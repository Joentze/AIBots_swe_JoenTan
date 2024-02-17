import { useConversation } from "@/app/customHooks/conversationHooks";
import { useEffect } from "react";

const MainChat = () => {
  const { conversationId, setConversationId } = useConversation();

  return <>{conversationId}</>;
};

export default MainChat;
