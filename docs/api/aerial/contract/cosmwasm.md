<a id="kiipy.aerial.contract.cosmwasm"></a>

# kiipy.aerial.contract.cosmwasm

Cosmwasm contract store, instantiate, execute messages.

<a id="kiipy.aerial.contract.cosmwasm.create_cosmwasm_store_code_msg"></a>

#### create`_`cosmwasm`_`store`_`code`_`msg

```python
def create_cosmwasm_store_code_msg(contract_path: str,
                                   sender_address: Address) -> MsgStoreCode
```

Create cosmwasm store code message.

**Arguments**:

- `contract_path`: contract path
- `sender_address`: sender address

**Returns**:

cosmwasm store code message

<a id="kiipy.aerial.contract.cosmwasm.create_cosmwasm_instantiate_msg"></a>

#### create`_`cosmwasm`_`instantiate`_`msg

```python
def create_cosmwasm_instantiate_msg(
        code_id: int,
        args: Any,
        label: str,
        sender_address: Address,
        funds: Optional[str] = None,
        admin_address: Optional[Address] = None) -> MsgInstantiateContract
```

Create cosmwasm instantiate message.

**Arguments**:

- `code_id`: code id
- `args`: args
- `label`: label
- `sender_address`: sender address
- `funds`: funds, defaults to None
- `admin_address`: admin address, defaults to None

**Returns**:

cosmwasm instantiate message

<a id="kiipy.aerial.contract.cosmwasm.create_cosmwasm_migrate_msg"></a>

#### create`_`cosmwasm`_`migrate`_`msg

```python
def create_cosmwasm_migrate_msg(code_id: int, args: Any,
                                contract_address: Address,
                                sender_address: Address) -> MsgMigrateContract
```

Create cosmwasm migrate message.

**Arguments**:

- `code_id`: code id
- `args`: args
- `contract_address`: sender address
- `sender_address`: sender address

**Returns**:

cosmwasm migrate message

<a id="kiipy.aerial.contract.cosmwasm.create_cosmwasm_execute_msg"></a>

#### create`_`cosmwasm`_`execute`_`msg

```python
def create_cosmwasm_execute_msg(
        sender_address: Address,
        contract_address: Address,
        args: Any,
        funds: Optional[str] = None) -> MsgExecuteContract
```

Create cosmwasm execute message.

**Arguments**:

- `sender_address`: sender address
- `contract_address`: contract address
- `args`: args
- `funds`: funds, defaults to None

**Returns**:

cosmwasm execute message

<a id="kiipy.aerial.contract.cosmwasm.create_cosmwasm_update_admin_msg"></a>

#### create`_`cosmwasm`_`update`_`admin`_`msg

```python
def create_cosmwasm_update_admin_msg(sender_address: Address,
                                     contract_address: Address,
                                     new_admin: Address) -> MsgExecuteContract
```

Create cosmwasm update admin message.

**Arguments**:

- `sender_address`: sender address
- `contract_address`: contract address
- `sender_address`: sender address
- `new_admin`: new admin address

**Returns**:

cosmwasm update admin message

<a id="kiipy.aerial.contract.cosmwasm.create_cosmwasm_clear_admin_msg"></a>

#### create`_`cosmwasm`_`clear`_`admin`_`msg

```python
def create_cosmwasm_clear_admin_msg(
        sender_address: Address,
        contract_address: Address) -> MsgExecuteContract
```

Create cosmwasm clear admin message.

**Arguments**:

- `sender_address`: sender address
- `contract_address`: contract address
- `sender_address`: sender address

**Returns**:

cosmwasm clear admin message

