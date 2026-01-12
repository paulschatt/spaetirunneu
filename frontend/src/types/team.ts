import Spaetirun from "spaetirun";

export interface Team {
    id: string
    name: string
    spaetirun: Spaetirun
    created_at: string
}

export interface TeamCreate {
    name: string
    spaetirun: Spaetirun
}

export interface TeamUpdate {
    name: string
    spaetirun: Spaetirun
}


