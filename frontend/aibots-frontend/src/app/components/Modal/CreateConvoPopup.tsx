import { useDisclosure } from "@mantine/hooks";
import { Modal, Button, Input, JsonInput } from "@mantine/core";
import { IoAdd } from "react-icons/io5";
import { useState } from "react";
import { useConversation } from "@/app/customHooks/conversationHooks";

const defaultParams = {
  model: "gpt-4",
};

const CreateConvoPopup = () => {
  const { conversationId, setConversationId } = useConversation();
  const [opened, { open, close }] = useDisclosure(false);
  const [jsonValue, setJsonValue] = useState(JSON.stringify(defaultParams));
  return (
    <>
      <Modal opened={opened} onClose={close} title="Create a Conversation 📝">
        <Modal.Body>
          <Input.Wrapper
            label="Conversation Name"
            description="Organise your conversations by giving it a unique name!"
          >
            <Input placeholder="Example:'an Exploration into Large Language Models'" />
          </Input.Wrapper>
          <br></br>

          <Input.Wrapper
            label="Conversation Name"
            description="Organise your conversations by giving it a unique name!"
          >
            <JsonInput value={jsonValue} onChange={setJsonValue} mt={8} />
          </Input.Wrapper>
          <br></br>
          <Button fullWidth>Create!</Button>
        </Modal.Body>
      </Modal>

      <Button leftSection={<IoAdd />} onClick={open}>
        Add Conversation
      </Button>
    </>
  );
};

export default CreateConvoPopup;
