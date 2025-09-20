
erDiagram

dim_Fecha ||--|{ ft_policytrans_ss: 
    "Id_Fecha_Transaccion
    Id_Fecha_Efectiva"
dim_Asegurado_d ||--|{ ft_policytrans_ss: 
    "Id_Asegurado"

link_cobertura_item_ss ||--|| ft_policytrans_ss: "Id_Item"

dim_cobertura_auto_ss ||--|| link_cobertura_item_ss:
    "Id_Item"
dim_cobertura_auto_ss

dim_policy_transaction_type ||--|{ ft_policytrans_ss: contains
dim_employee ||--|{ ft_policytrans_ss: contains
dim_policy_transaction_audit ||--|{ ft_policytrans_ss: contains

%% ft: facto, ss: frecuencia carga(segundos)
ft_policytrans_ss {
    string Id_Fecha_Transaccion fk   
    %% se conecta con date_key
    string Id_Fecha_Efectiva fk     
    %% se conecta con date_key
    string policyHolder_key fk
    string Id_Empleado fk
    string Id_Covertura fk
    string Id_item fk
    string policy_transation_type_key fk
    string policy_transaction_audit_key fk
    string policy_number
    string policy_transaction_number
    string policy_transaction_dollar_amount
}

dim_Fecha {
    string date_key pk
    int year
    int month
    int day
    string dow
    holiday bool
}

dim_Asegurado_d {
    date Fecha_Edit
    string Id_Asegurado pk
    string Nombre_Completo
    string date_of_birth 
    string gender  
    int Cod_postal
    string Desc_Segmento_Hist
    string Desc_Segmento
    string Estado_Civil
}



link_item_cobertura_ss {
    string Id_Item pk
}

dim_cobertura_auto_ss {
    string Id_Item pk
    string Desc_Marca
    int Ano_Fabricacion
    string Desc_clasificacion
    float Valuacion
}


dim_cobertura_inmu_ss {
    string Id_Item pk
    Int Metros_Cuadrados
    date Fecha_Construccion
    string Cod_Postal
    float Valuacion
}

dim_cobertura_pers_ss {
    string Id_Item pk
    string Desc_Item
    float Valuacion
}



dim_policy_transaction_type {
    date Fecha_Edit
    string id_Transation_Type pk
    string Type_Description 
    %% Nueva poliza / cancelacion, etc
    string etc
}

dim_employee {
    string id
    string FullName
    string etc
}

%% toda metadata
dim_policy_transaction_audit { 
    string id_Transaction pk
    string etl_ts
    etc dvd
}

POLICY_RATING {
    int rating
    string efe
}
