from fastapi import HTTPException, status
from app.utils.enum.enum_role import RoleEnum


class ResponseHandler:
    @staticmethod
    def success(message, data=None):
        return {"message": message, "data": data}

    @staticmethod
    def get_single_success(name, id, data):
        message = f"Details for {name} with id {id}"
        return ResponseHandler.success(message, data)

    @staticmethod
    def create_success(name, id, data):
        message = f"{name} with id {id} created successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def update_success(name, id, data):
        message = f"{name} with id {id} updated successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def delete_success(name, id, data):
        message = f"{name} with id {id} deleted successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def not_found_error(name="", id=None):
        message = f"{name} With Id {id} Not Found!"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    
    @staticmethod
    def already_exist_error(name="", id=None):
        message = f"{name} With Id {id} Already Exist!"
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=message)
    
    @staticmethod
    def bad_request(message=None):
        message = f"{message}"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
    
    @staticmethod
    def is_not_active(name=""):
        message = f"{name} Not Active!"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
    
    @staticmethod
    def is_not_investor(name=""):
        message = f"{name} Not Role {RoleEnum.INVESTOR.value}!"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
    
    def invalid_amount_bid(message=""):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
    
    @staticmethod
    def is_not_operator(name=""):
        message = f"{name} Not Role {RoleEnum.OPERATOR.value}!"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

    @staticmethod
    def invalid_token(name=""):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid {name} token.",
            headers={"WWW-Authenticate": "Bearer"})

    @staticmethod
    def invalid_credentials():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    @staticmethod
    def insufficient_permissions(name=""):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Insufficient permissions",
            headers={"WWW-Authenticate": "Bearer"},
        )